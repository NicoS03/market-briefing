"""Generate assets/numbers.tex and assets/data/*.dat for main.tex.

Every number that appears on a slide is defined here exactly once.
* FSR Chart 2.4b values are read from the ECB chart-data annex (data/raw/fsr202611_chapter2_data.xlsx).
* US Treasury yields are read from the US Treasury daily par yield CSV (data/raw/ust_par_yields_2026.csv).
* Values that only exist in releases or news articles are typed in the MANUAL dict, each with its source key
  (see SOURCES.md for URL, publication date and retrieval date).

Run with a Python that has openpyxl:  python make_assets.py
"""
import csv
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent
RAW = ROOT / "data" / "raw"
OUT = ROOT / "assets"
(OUT / "data").mkdir(parents=True, exist_ok=True)

macros = {}  # name -> (value string, source comment)


def define(name, value, source):
    assert name.isalpha(), name
    assert name not in macros, f"duplicate macro {name}"
    macros[name] = (value, source)


# ---------------------------------------------------------------- manual values (releases and news)
MANUAL = [
    # Eurostat euro indicators, 18 Nov 2026 (final) and 4 Nov 2026 (flash)
    ("HicpOct", "4.0", "Eurostat 18 Nov 2026 [ES18]"),
    ("HicpSep", "3.8", "Eurostat 18 Nov 2026 [ES18]"),
    ("HicpPeakPrev", "4.3", "Eurostat HICP, Sep 2023 (prc_hicp_manr) [ESAPI]"),
    ("CoreOct", "2.6", "Eurostat 18 Nov 2026, all-items excl. energy, food, alcohol & tobacco [ES18]"),
    ("CoreFlash", "2.5", "Eurostat flash 4 Nov 2026 [ES04]"),
    ("EnergyOct", "21.0", "Eurostat 18 Nov 2026 [ES18]"),
    ("EnergyFlash", "20.8", "Eurostat flash 4 Nov 2026 [ES04]"),
    # ECB policy rates
    ("EcbDfr", "2.50", "ECB monetary policy decisions 29 Oct 2026 [ECBMP1029]"),
    ("EcbProbHike", "91", "LSEG via Trading Economics, commentary of 18 Nov 2026 [TE]"),
    # Fed
    ("FedLow", "3.75", "FOMC statement 28 Oct 2026 [FOMC1028]"),
    ("FedHigh", "4.00", "FOMC statement 28 Oct 2026 [FOMC1028]"),
    ("FedProbHikeLseg", "98", "LSEG via Trading Economics, commentary of 18 Nov 2026 [TE]"),
    ("FedProbHikeCme", "95", "CME FedWatch via CNBC, 18 Nov 2026 [CNBC18]"),
    ("UsCpiMoM", "0.4", "StockAnalysis 10 Nov 2026 citing BLS [SA-CPI]"),
    ("UsCpiExp", "0.3", "StockAnalysis 10 Nov 2026, Dow Jones consensus [SA-CPI]"),
    ("UsCoreMoM", "0.3", "StockAnalysis 10 Nov 2026 citing BLS [SA-CPI]"),
    # German Bund
    ("BundTenNow", "3.41", "Trading Economics 19 Nov 2026 [TE]; Reuters via Rallies 19 Nov 2026 [RALLIES]"),
    ("BundTenPeak", "3.653", "Reuters via Rallies 19 Nov 2026 (17-year high, late Sep) [RALLIES]"),
    # France
    ("OatSpreadNow", "153", "Reuters via Rallies 19 Nov 2026 [RALLIES]"),
    ("OatSpreadPeak", "177", "Reuters via AOL 16 Nov 2026 (late Oct, highest since Nov 2011) [AOL16]"),
    ("BtpSpreadSeventeen", "105", "SoldiOnline 17 Nov 2026, closing level [SOLDI]"),
    # 12 Nov opening snapshot, QuiFinanza 12 Nov 2026 [QUIFIN]
    ("YBund", "3.31", "QuiFinanza 12 Nov 2026, opening [QUIFIN]"),
    ("YBtp", "4.35", "QuiFinanza 12 Nov 2026, opening [QUIFIN]"),
    ("YOat", "4.79", "QuiFinanza 12 Nov 2026, opening [QUIFIN]"),
    ("YBono", "3.88", "QuiFinanza 12 Nov 2026, opening [QUIFIN]"),
    # Investor base, ECB FSR press briefing slides 18 Nov 2026, slide 8 (Eurostat, ECB QSA)
    ("HoldCbOld", "34.9", "ECB FSR press briefing 18 Nov 2026, slide 8, 2022 [ECBSP]"),
    ("HoldCbNew", "21.5", "ECB FSR press briefing 18 Nov 2026, slide 8, Q2 2026 [ECBSP]"),
    ("HoldForOld", "20.0", "ECB FSR press briefing 18 Nov 2026, slide 8, 2022 [ECBSP]"),
    ("HoldForNew", "25.1", "ECB FSR press briefing 18 Nov 2026, slide 8, Q2 2026 [ECBSP]"),
    # US data calendar, Yahoo Finance 19 Nov 2026 [YAHOO]
    ("PceFcst", "0.3", "Yahoo Finance 19 Nov 2026, consensus core PCE m/m [YAHOO]"),
    ("GdpFcst", "3.4", "Yahoo Finance 19 Nov 2026, consensus Q3 GDP 2nd estimate [YAHOO]"),
]
for name, value, src in MANUAL:
    define(name, value, src)

# ---------------------------------------------------------------- QuiFinanza snapshot: spreads in bp
bund = float(macros["YBund"][0])
spreads = []
for name, label in [("YBtp", "Italy (BTP)"), ("YOat", "France (OAT)"), ("YBono", "Spain (Bono)")]:
    s = round((float(macros[name][0]) - bund) * 100)
    spreads.append((label, s))
    define("S" + name[1:], str(s), "computed: yield minus Bund, QuiFinanza 12 Nov 2026 [QUIFIN]")
# reported spreads in the article: BTP 104, OAT 148, Bono 57
assert [s for _, s in spreads] == [104, 148, 57], spreads

# ---------------------------------------------------------------- US Treasury par yields
rows = {r["Date"]: r for r in csv.DictReader(open(RAW / "ust_par_yields_2026.csv", encoding="utf-8"))}
d_now, d_wk0, d_wk1 = "11/19/2026", "11/06/2026", "11/13/2026"
for tenor, tag in [("2 Yr", "Two"), ("10 Yr", "Ten"), ("30 Yr", "Thirty")]:
    define("Ust" + tag + "Now", f"{float(rows[d_now][tenor]):.2f}", "US Treasury par yield, 19 Nov 2026 [UST]")
for tenor, tag in [("2 Yr", "Two"), ("10 Yr", "Ten")]:
    chg = round((float(rows[d_wk1][tenor]) - float(rows[d_wk0][tenor])) * 100)
    define("Ust" + tag + "Week", f"{chg:d}", "US Treasury par yield change 6 Nov to 13 Nov 2026, bp [UST]")

# ---------------------------------------------------------------- FSR Chart 2.4 panel b (ECB annex)
wb = openpyxl.load_workbook(RAW / "fsr202611_chapter2_data.xlsx", read_only=True, data_only=True)
ws = wb["Chart 2.4"]
cells = [[c for c in r] for r in ws.iter_rows(values_only=True)]


def row_after(header_substr, region):
    """Return the numeric values of the row labelled `region` that follows a header containing header_substr."""
    for i, r in enumerate(cells):
        for j, c in enumerate(r):
            if isinstance(c, str) and c.startswith(header_substr):
                for r2 in cells[i + 1:i + 3]:
                    if r2[j - 1] == region:  # region label sits one column left of the header
                        return [float(v) for v in r2[j:j + 3]]
    raise KeyError(header_substr, region)


# Model decomposition: expectations + term premium (sums to the model-fitted yield change)
ea_m = row_after("10-year OIS change", "EA")      # [total, expectations, term premium]
us_m = row_after("10-year UST change", "US")
# Fisher split: inflation compensation + real rate (sums to the observed yield change)
ea_f = row_after("Fitted 10-year OIS", "EA")      # [total, inflation, real]
us_f = row_after("Fitted 10-year UST", "US")
ea_30 = row_after("30-year OIS", "EA")            # [total, inflation, real]
us_30 = row_after("30-year UST", "US")

# The annex header labels are attached to the other block: the expectations/term-premium split adds up to
# the total printed under "Fitted ...", the inflation/real split to the total printed under "... change".
fitted = {"EA": ea_m[1] + ea_m[2], "US": us_m[1] + us_m[2]}
observed = {"EA": ea_f[1] + ea_f[2], "US": us_f[1] + us_f[2]}
assert abs(fitted["EA"] - ea_f[0]) < 0.05 and abs(observed["EA"] - ea_m[0]) < 0.05
assert abs(fitted["US"] - us_f[0]) < 0.05 and abs(observed["US"] - us_m[0]) < 0.05

src = "ECB FSR Nov 2026 chart data annex, Chart 2.4b, 1 Jan to 10 Nov 2026 (US to 9 Nov) [FSRDATA]"
define("EaExp", f"{ea_m[1]:.0f}", src); define("EaTp", f"{ea_m[2]:.0f}", src)
define("EaInfl", f"{ea_f[1]:.0f}", src); define("EaReal", f"{ea_f[2]:.0f}", src)
define("EaFitted", f"{fitted['EA']:.1f}", src); define("EaObserved", f"{observed['EA']:.1f}", src)
define("UsExp", f"{us_m[1]:.0f}", src); define("UsTp", f"{us_m[2]:.0f}", src)
define("UsInfl", f"{us_f[1]:.0f}", src); define("UsReal", f"{us_f[2]:.0f}", src)
define("UsFitted", f"{fitted['US']:.1f}", src); define("UsObserved", f"{observed['US']:.1f}", src)

with open(OUT / "data" / "fsr24b.dat", "w", encoding="utf-8") as f:
    f.write("% ECB FSR November 2026, Chart 2.4 panel b, chart data annex. bp, 1 Jan to 10 Nov 2026.\n")
    f.write("% x: 0 EA 10y model, 1 US 10y model, 3 EA 10y Fisher, 4 US 10y Fisher, 6 EA 30y Fisher, 7 US 30y Fisher\n")
    f.write("% exp/tp: model split (sums to fitted change); infl/real: Fisher split (sums to observed change)\n")
    f.write("x exp tp infl real total\n")
    for x, (e, t) in [(0, ea_m[1:]), (1, us_m[1:])]:
        f.write(f"{x} {e:.2f} {t:.2f} 0 0 {e + t:.2f}\n")
    for x, (i, r) in [(3, ea_f[1:]), (4, us_f[1:]), (6, ea_30[1:]), (7, us_30[1:])]:
        f.write(f"{x} 0 0 {i:.2f} {r:.2f} {i + r:.2f}\n")

with open(OUT / "data" / "spreads.dat", "w", encoding="utf-8") as f:
    f.write("% 10-year spreads to the Bund, bp, QuiFinanza 12 Nov 2026 opening\nx label spread\n")
    for i, (label, s) in enumerate(spreads):
        f.write(f"{i} {{{label}}} {s}\n")

# ---------------------------------------------------------------- write numbers.tex
with open(OUT / "numbers.tex", "w", encoding="utf-8") as f:
    f.write("% Generated by make_assets.py. Do not edit by hand. Sources: see SOURCES.md.\n")
    for name, (value, source) in macros.items():
        f.write(f"\\newcommand{{\\{name}}}{{{value}}}% {source}\n")
print(f"wrote {len(macros)} macros")
for k, (v, _) in macros.items():
    print(f"  {k} = {v}")
