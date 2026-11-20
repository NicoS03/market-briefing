# SOURCES

Every number on the slides, with its source, URL, publication date and retrieval date. All sources were retrieved on **20 November 2026**. Each number is defined once as a macro in `assets/numbers.tex`, which `make_assets.py` generates. The macro name is given in brackets.

Source keys:

| Key | Source | URL | Published |
|---|---|---|---|
| ES18 | Eurostat, "Annual inflation up to 4.0% in the euro area" (final HICP, October) | https://ec.europa.eu/eurostat/web/products-euro-indicators/w/2-18112026-ap | 18 Nov 2026 |
| ES04 | Eurostat, "Euro area annual inflation up to 4.0%" (flash) | https://ec.europa.eu/eurostat/web/products-euro-indicators/w/2-04112026-ap | 4 Nov 2026 |
| ESHIST | Eurostat HICP annual rates: database prc_hicp_manr (2023 to Dec 2025) and euro indicators releases 2-25022026-ap (Jan 1.7%), 2-18032026-ap (Feb 1.9%), 2-16042026-ap (Mar 2.6%), 2-20052026-ap (Apr 3.0%); May to Sep 2026 from the table in ES18 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/prc_hicp_manr?geo=EA&coicop=CP00 and the release URLs above | various |
| FSR | ECB, Financial Stability Review, November 2026 (PDF, Section 2.2, Charts 2.1, 2.4, 2.5, 2.6, Box 7) | https://www.ecb.europa.eu/press/financial-stability-publications/fsr/pdf/ecb.fsr202611~e03b919d36.en.pdf | 18 Nov 2026 |
| FSRDATA | ECB, FSR November 2026 chart data annex, "Chapter 2.xlsx", sheet "Chart 2.4" (copy in `data/raw/`) | https://www.ecb.europa.eu/press/financial-stability-publications/fsr/pdf/ecb.fsr202611_annex~46d8759e78.en.zip | 18 Nov 2026 |
| ECBPR | ECB press release on the FSR | https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.pr261118~83c5c60158.en.html | 18 Nov 2026 |
| ECBSP | ECB, FSR November 2026 press briefing slides, slide 8 | https://www.ecb.europa.eu/press/key/date/2026/html/ecb.sp261118~86f1e8147e.en.pdf | 18 Nov 2026 |
| ECBMP1029 | ECB, Monetary policy decisions (rates unchanged) | https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.mp261029~9a493adf17.en.html | 29 Oct 2026 |
| ECBMP0910 | ECB, Monetary policy decisions (+25 bp, effective 16 Sep) | https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.mp260910~314e508016.en.html | 10 Sep 2026 |
| ECBDFR | ECB Data Portal API, deposit facility rate (2.00 to 2.25 on 17 Jun 2026, 2.50 on 16 Sep 2026) | https://data-api.ecb.europa.eu/service/data/FM/D.U2.EUR.4F.KR.DFR.LEV | retrieved 20 Nov 2026 |
| ECBCAL | ECB weekly schedule (Lagarde keynote, 20 Nov) and Governing Council calendar (16 and 17 Dec) | https://www.ecb.europa.eu/press/calendars/weekly/html/index.en.html ; https://www.ecb.europa.eu/press/calendars/mgcgc/html/index.en.html | retrieved 20 Nov 2026 |
| FOMC0916 | Federal Reserve, FOMC statement (+25 bp to 3.75 to 4 percent) | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm | 16 Sep 2026 |
| FOMC1028 | Federal Reserve, FOMC statement (hold; Cook and Hammack dissent for +25 bp) | https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm | 28 Oct 2026 |
| FOMCCAL | Federal Reserve, FOMC meeting calendar (8 and 9 Dec, with projections; October minutes released 18 Nov) | https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm | retrieved 20 Nov 2026 |
| UST | US Treasury, daily par yield curve rates 2026 (copy in `data/raw/`) | https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve | retrieved 20 Nov 2026 |
| TE | Trading Economics, Germany 10-year bond yield (quote and commentary) | https://tradingeconomics.com/germany/government-bond-yield | 19 Nov 2026 (quote); the probability paragraph was written on 18 Nov |
| CNBC18 | CNBC, "Longer-dated Treasury yields fall as traders weigh Waller comments, Fed minutes" | https://www.cnbc.com/amp/2026/11/18/treasury-yields-bonds-fed.html | 18 Nov 2026 |
| SA-CPI | StockAnalysis (K. Gunnars), US CPI October 2026, citing BLS | https://stockanalysis.com/news/us-cpi-rises-october-2026/ | 10 Nov 2026 |
| RALLIES | Reuters via Rallies, "Euro zone bond yields tick up as markets digest Anthropic's debut" | https://rallies.ai/news/euro-zone-bond-yields-tick-up-as-markets-digest-anthropics-debut-0feec10836584447 | 19 Nov 2026 |
| AOL16 | Reuters (S. Rebaudo) via AOL, "Euro zone yields edge up as traders bet on three ECB hikes by late 2027" | https://www.aol.com/articles/euro-zone-yields-rise-traders-105053000.html | 16 Nov 2026 |
| QUIFIN | QuiFinanza, "Spread Btp-Bund a 104 punti base, rendimenti a 4,35%" (opening table, 12 Nov) | https://quifinanza.it/economia/finanza/spread-btp-bund-12-novembre-2026/1023908/ | 12 Nov 2026 |
| SOLDI | SoldiOnline, "Spread Btp-Bund a 105 punti" (close) | https://www.soldionline.it/?p=183911 | 17 Nov 2026 |
| YAHOO | Yahoo Finance (Simply Wall St), "US Stock Market Today" (data calendar) | https://finance.yahoo.com/markets/stocks/articles/us-stock-market-today-p-131516375.html | 19 Nov 2026 |

## Slide 1 (Inflation)

| Number on slide | Value | Date of data | Source | Macro |
|---|---|---|---|---|
| Euro area HICP, October | 4.0% | Oct 2026 (final, 18 Nov) | ES18 (flash ES04 also 4.0%) | HicpOct |
| Highest since September 2023 | Sep 2023: 4.3%. Every later month is below 4.0% (max 3.8% in Sep 2026) | 2023 to 2026 | ESHIST, ES18 | HicpPeakPrev |
| Core (excl. energy, food, alcohol, tobacco) | 2.6% (flash 2.5%) | Oct 2026 | ES18 table; ES04 | CoreOct |
| Energy | 21.0% (flash 20.8%) | Oct 2026 | ES18 | EnergyOct |
| US CPI m/m | +0.4% | Oct 2026 | SA-CPI (citing BLS, 10 Nov) | UsCpiMoM |
| US CPI expected | 0.3% (Dow Jones poll) | Oct 2026 | SA-CPI | UsCpiExp |
| ECB deposit rate | 2.50% | since 16 Sep 2026, held 29 Oct | ECBMP1029, ECBMP0910, ECBDFR | EcbDfr |
| Next ECB decision | 17 Dec | 2026 | ECBCAL | |
| P(ECB +25 bp, 17 Dec) | 91% | 18 Nov 2026 | TE (LSEG) | EcbProbHike |
| Fed funds range | 3.75% to 4.00% | since 16 Sep 2026, held 28 Oct | FOMC0916, FOMC1028 | FedLow, FedHigh |
| Next Fed decision | 9 Dec | 2026 | FOMCCAL | |
| P(Fed +25 bp, 9 Dec) | 95% (CME FedWatch) to 98% (LSEG) | 18 Nov 2026 | CNBC18; TE | FedProbHikeCme, FedProbHikeLseg |
| Figure | FSR Chart 2.5, panel a (vector crop, PDF page 45) | 1 Jan 2024 to 31 Dec 2027 | FSR | |

## Slide 2 (Yields)

| Number on slide | Value | Date of data | Source | Macro |
|---|---|---|---|---|
| Bund 10y | 3.41% | 19 Nov 2026 | TE (also RALLIES) | BundTenNow |
| US 10y | 5.04% | 19 Nov 2026 | UST | UstTenNow |
| US 2y, week to 13 Nov | +37 bp (4.51% on 6 Nov to 4.88% on 13 Nov) | 6 to 13 Nov 2026 | UST | UstTwoWeek |
| US 10y, week to 13 Nov | +29 bp (4.86% to 5.15%) | 6 to 13 Nov 2026 | UST | UstTenWeek |
| "Near post-GFC highs" | text | to 10 Nov 2026 | FSR Section 2.2, Chart 2.4a | |
| Chart, EA 10y model split | expectations 24.2, term premium 22.3, sum (fitted) 46.5 bp | 1 Jan to 10 Nov 2026 | FSRDATA | EaExp, EaTp, EaFitted |
| Chart, US 10y model split | expectations 58.9, term premium 11.3, sum (fitted) 70.2 bp | 1 Jan to 9 Nov 2026 | FSRDATA | UsExp, UsTp, UsFitted |
| Chart, EA 10y Fisher split | inflation 21.5, real 25.3, sum (observed) 46.8 bp | 1 Jan to 10 Nov 2026 | FSRDATA | EaInfl, EaReal, EaObserved |
| Chart, US 10y Fisher split | inflation -2.0, real 75.8, sum (observed) 73.8 bp | 1 Jan to 9 Nov 2026 | FSRDATA | UsInfl, UsReal, UsObserved |
| Chart, 30y Fisher split | EA: inflation 10.0, real 0.4, sum 10.4; US: inflation -4.0, real 48.6, sum 44.6 bp | as above | FSRDATA | (data file only) |

The chart labels are rounded to whole basis points: 47, 70, 47, 74, 10, 45.

## Slide 3 (Spreads)

| Number on slide | Value | Date of data | Source | Macro |
|---|---|---|---|---|
| OAT-Bund spread | 153 bp (France 4.94%, Germany 3.41%) | 19 Nov 2026 | RALLIES | OatSpreadNow |
| OAT-Bund peak | 177 bp, late October, highest since November 2011 | late Oct 2026 | AOL16 (RALLIES: "peak above 170") | OatSpreadPeak |
| Central bank share of EA sovereign debt | 21.5% (34.9% in 2022) | Q2 2026 | ECBSP slide 8 (Eurostat, ECB QSA) | HoldCbNew, HoldCbOld |
| Foreign investor share | 25.1% (20.0% in 2022) | Q2 2026 | ECBSP slide 8 | HoldForNew, HoldForOld |
| Quote "the risk of abrupt repricing episodes" | 6 words | 18 Nov 2026 | ECBPR | |
| Bar chart: BTP-Bund | 104 bp (BTP 4.35%, Bund 3.31%) | 12 Nov 2026, opening | QUIFIN | YBtp, YBund, SBtp |
| Bar chart: OAT-Bund | 148 bp (OAT 4.79%) | 12 Nov 2026, opening | QUIFIN | YOat, SOat |
| Bar chart: Bono-Bund | 57 bp (Bono 3.88%) | 12 Nov 2026, opening | QUIFIN | YBono, SBono |
| Figure | Spread chart, 1 Jan 2007 to 10 Nov 2026 (same data as FSR Chart 2.5b), vector crop | 18 Nov 2026 | ECBSP slide 8 | |

The bar spreads are computed in `make_assets.py` as yield minus Bund, and the script checks them against the spreads printed in the article (104, 148, 57).

## Slide 4 (Outlook)

| Item on slide | Value | Source | Macro |
|---|---|---|---|
| Lagarde keynote, European Banking Congress | Fri 20 Nov 2026 (no text published at retrieval) | ECBCAL | |
| US core PCE and Q3 GDP second estimate | Wed 25 Nov 2026; consensus core PCE 0.3% m/m, GDP 3.4% (footnote) | YAHOO | PceFcst, GdpFcst |
| Euro area flash HICP, November | Tue 1 Dec 2026 | ES18 ("next flash estimate ... 1 December 2026") | |
| FOMC decision and projections | Wed 9 Dec 2026 (meeting 8 and 9 Dec) | FOMCCAL | |
| ECB decision | Thu 17 Dec 2026 | ECBCAL | |
| Probabilities 91%, 95% to 98% | as on slide 1 | TE, CNBC18 | |
| OAT-Bund 153 bp | as on slide 3 | RALLIES | |

## Text on slides that comes from the FSR (no numbers)

* Energy lifts short-term, not medium-term, inflation compensation: FSR Section 2.2, p. 44 of the PDF, Chart 2.5 title.
* Model and Fisher decompositions, and the real rate definitions: FSR Chart 2.4 notes.
* Term-structure models: Joslin, Singleton and Zhu (2011); Geiger and Schupp (2018); Adrian, Crump and Moench (2013); Christensen and Rudebusch (2012); D'Amico, Kim and Wei (2018). Bibliographic details are taken from the FSR Chart 2.4 notes and match the published articles.

## Speaker-notes only (not on slides)

* Conflict timeline: war from 2 March 2026 (first trading day after the 28 February start), ceasefire 7 April, ceasefire breakdown 27 June. Source: FSR Chart 2.1 notes.
* ECB hikes in June and September 2026: ECBDFR (effective 17 Jun and 16 Sep).
* Quarter of euro area debt maturing before end-2028; Japanese and Dutch pension demand; hedge fund repo (Box 7): FSR Section 2.2, pp. 45 to 46 and Box 7.

## Checked but not used, or dropped

| Claim or URL | Status |
|---|---|
| CME FedWatch, about 10% chance of a 50 bp Fed hike, 19 Nov | **Not verified.** The CME page cannot be read without a browser. The only figure found was 9.1% about 11 Nov (Stocktwits, a blog), before Waller called for 50 bp on 18 Nov. Left out. |
| Nuveen weekly commentary (2y +33 bp, 10y +28 bp) | Page blocks automated access (request blocked). Replaced with US Treasury data: +37 bp and +29 bp. |
| Investing.com (13 and 19 Nov, both URLs) | HTTP 403 for automated access. Not used. |
| FRED T10Y2Y | Connection reset from this machine. US Treasury par yields used instead (primary source). |
| CNBC 17 Nov | No URL given and none found. Not used. |
| ABA Banking Journal (7 Oct) and Wealth Management (28 Oct) | Both open and confirm the September hike and the 10 to 2 October hold. Superseded by the FOMC statements, so they are not in the references. |
| Admiral Markets | Not used, as instructed. |
