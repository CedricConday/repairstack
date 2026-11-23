# Survey of existing open software and data: remyelination trials and imaging in MS

Survey date: 2026-11-23. Every fact below was checked against a live source on that date unless it sits in section 3 ("Not verified"). "Last activity" is the last push or release for code, the publication or record-update date for papers and registry entries.

Sources used: GitHub API (repository and code search), Zenodo API, Dryad API, OSF API, OpenNeuro GraphQL, ClinicalTrials.gov API v2, PubMed, publisher and project pages.

## 1. Verdicts

| Tool | Verdict |
|---|---|
| A. Evidence map of remyelination trials | **Partly exists, here is the gap.** Two 2025 systematic reviews hold trial tables, and the registry is machine-readable, but there is no open, maintained, machine-readable table that joins drug, mechanism, population, primary outcome and result for every trial. |
| B. Imaging measure of myelin repair per lesion, tested against a known answer | **Partly exists, here is the gap.** The map-fitting step (MTR, MTsat, qMT, MWF, QSM) is well covered by maintained toolboxes with simulation tests, and lesion segmentation is covered. No open tool measures per-lesion change over time in a myelin metric and ships a known-answer test for that step, and no open MS dataset has repeated myelin-sensitive MRI. |
| C. Responder re-analysis of the small trials | **Does not exist as open data or code.** No individual-participant data is publicly deposited for any of the four trial programmes. All routes are by request. No open responder or heterogeneity-of-effect code was found. |

## 2. Tables

### Tool A: evidence map

| Name | Link | What it is | Machine-readable | Licence | Last activity | What it lacks for our purpose |
|---|---|---|---|---|---|---|
| Systematic review of remyelinating interventions and approved DMTs (Eur J Neurol) | https://doi.org/10.1111/ene.70397 (PMC12603786) | Table 1: 23 rows of completed or terminated trials with drug, mode of action, population, outcome measures, results. Table 2: 18 rows of starting or ongoing trials. Last search July 2025. | Tables in the article HTML; one xlsx supplement (49 KB) and one docx. | CC BY-NC-ND 4.0 | Published 2025-11-11 | One-off, not living. No-derivatives licence blocks redistributing a reworked table. Rows are not one-per-trial (some drugs repeat). Closest existing match. |
| Systematic review of clinical trials of remyelination interventions (Neurol Res) | https://doi.org/10.1080/01616412.2025.2507756 | 25 trials, 3,341 participants, 17 interventions; outcomes limited to MTR, VEP, MWF, DTI, OCT. Search May 2024. | No. Tables inside a paywalled article. | Publisher copyright | Published online 2025-05-20 | Paywalled, static, search already 2.5 years old. |
| Systematic review of neuroprotective and neuroregenerative strategies (Mult Scler J) | https://pmc.ncbi.nlm.nih.gov/articles/PMC8688986 | 19 clinical studies plus 250 animal studies; study list in a supplementary PDF. Search to 2020-01-16. | No (PDF supplement). | CC BY-NC 4.0 | Published 2021-04-19 | Old, PDF only, intervention-level summaries. |
| Narrative reviews of the trial pipeline | Drugs 2025: https://doi.org/10.1007/s40265-025-02212-x ; Curr Opin Neurol 2025: https://doi.org/10.1097/wco.0000000000001363 | Trial design review with status as of 2025-05-15; review of 67 trials of novel MS therapies with a remyelinating category. | No. | Publisher copyright | 2025 | Narrative, static. |
| ClinicalTrials.gov API v2 | https://clinicaltrials.gov/api/v2/studies | Registry. A query for condition "multiple sclerosis" plus "remyelination OR remyelinating OR myelin repair" returned 66 records on 2026-11-23; 8 have posted results. | Yes (JSON, CSV). | Public domain (US government) | Live | No mechanism field. Results posted for 8 of 66. The 66 include imaging and observational studies. Trials registered only on ISRCTN or EudraCT (the bexarotene trial, for one) are missing. This is the raw feed, not a map. |
| MS-SOLES, a systematic online living evidence summary for progressive MS | Project record: https://doi.org/10.17605/osf.io/jbhxv ; app: https://camarades.shinyapps.io/ms-soles/ ; framework package: https://github.com/camaradesuk/solesR | Living, automated literature summary built to rank repurposing candidates for progressive MS trials. | App responds (HTTP 200); download function not confirmed. solesR is AGPL-3.0. | AGPL-3.0 (package) | OSF project created and last modified 2023-10-02; solesR pushed 2026-11-18 | Publication-level, not trial-level. Scope is progressive MS drug candidates, not remyelination trials with results. Current content and update date of the app not confirmed (see section 3). |
| Society pipeline pages | MS Canada: https://mscanada.ca/ms-research/ms-treatments-in-development | Web list of 11 entries (7 drugs) with phase. | No. No download. | Not stated | No update date shown | No remyelination category at all; immunology drugs only. |
| GitHub and Zenodo searches | n/a | Repository searches for remyelination trials, MS trial trackers, MS clinical trial datasets. | n/a | n/a | 2026-11-23 | No repository or dataset of this kind exists. The 11 GitHub repositories matching "remyelination" are all animal or cell analysis code. |

Gap for Tool A: a single openly licensed table, one row per trial, with registry identifier, drug, mechanism, population, primary outcome, result and source, regenerated from the registry and corrected by hand against the published papers.

### Tool B: imaging measure

Toolboxes that compute myelin-sensitive maps:

| Name | Link | What it computes | Per lesion over time | Known-answer validation | Licence | Last activity |
|---|---|---|---|---|---|---|
| qMRLab | https://github.com/qMRLab/qMRLab | MTR, MTsat, qMT (three acquisitions), MWF from multi-echo T2 or T2*, T1, T2. | No. Voxel maps only. | Yes for fitted models: built-in single-voxel simulation and sensitivity analysis compare fitted values with the inputs. Not available for MTsat or MTR (closed-form). | MIT | v3.0.0 on 2026-08-16; pushed 2026-11-10 |
| QUIT | repository "QUIT" on GitHub (65 stars) | Relaxometry, MT, qMT, mcDESPOT, steady-state methods; C++ command line. | No. | Simulation use not confirmed in this pass. | MPL-2.0 | Pushed 2026-06-24 |
| DECAES.jl | repository "DECAES.jl" on GitHub (41 stars) | MWF from multi-echo spin-echo T2 decomposition; Julia port of the UBC code. | No. | Not confirmed in this pass. | MIT | Pushed 2026-11-12 |
| hMRI toolbox | https://github.com/hMRI-group/hMRI-toolbox | MTsat, R1, R2*, PD from multi-parameter mapping; SPM-based. | No. | Not confirmed in this pass. | GPL-2.0 | v1.0.0 on 2026-04-21; pushed 2026-10-14 |
| QSMxT | https://github.com/QSMxT/QSMxT | End-to-end quantitative susceptibility mapping. | No. | Not confirmed in this pass. | GPL-3.0 | v12.2.0 on 2026-11-21 |
| SEPIA | repository "sepia" on GitHub (76 stars) | QSM pipelines, Matlab. | No. | Not confirmed. | MIT | Pushed 2026-11-10 |
| ihmt_proc | repository "ihmt_proc" on GitHub | Inhomogeneous MT preprocessing (denoise, Gibbs, motion). | No. | No. | No standard licence detected | Pushed 2026-10-06 |
| MRtrix3 (MP-PCA denoising) | https://github.com/MRtrix3/mrtrix3 | Denoising only; used ahead of MT and MWF fits. Not a myelin measure. | No. | n/a | MPL-2.0 | Pushed 2026-11-17 |
| Clinical MPM pipeline | https://clinicalmpm.github.io/ | Multi-parameter mapping protocol and pipeline standardised for MS research. | No. | Not confirmed. | Not checked | Paper 2024-12-16 |

Lesion handling and lesion-wise change:

| Name | Link | What it does | Myelin metric per lesion over time | Known-answer validation | Licence | Last activity |
|---|---|---|---|---|---|---|
| LST-AI | https://github.com/CompImg/LST-AI | Deep-learning MS lesion segmentation from T1 and FLAIR. | No. Cross-sectional masks. | Tested against manual masks only. | MIT | v1.1.0 on 2024-02-15; pushed 2026-08-20 |
| Small lesion-tracking repositories | GitHub: "LesionDelta", "MS-longitudinal-lesion-tracker", "brain-mri-radiomics-pipeline" | New-lesion detection or lesion change on FLAIR. | No myelin metric. | None stated. | MIT or none | 2026-07 to 2026-08; 0 stars each |
| Exponential recovery model for active lesions (ihMT paper) | https://doi.org/10.1162/imag_a_00235 | Fits onset loss, final value and recovery rate of ihMTR, MTR, RD and T1w per lesion over 12 months; 52 lesions, 9 patients. This is the nearest published "repair index". | Yes, in the paper. | No. Only the preprocessing wrapper is released; the lesion model code and data are "on request". | n/a | Published 2024 |
| Longitudinal MWF per lesion (mcDESPOT) | https://pmc.ncbi.nlm.nih.gov/articles/PMC9668603 | 386 lesions tracked over 4 time points with an automatic lesion follow-up algorithm; classifies lesions as increasing, decreasing, varying, invariant. | Yes, in the paper. | Scan-rescan only. In-house scripts, not released; authors state they cannot share data. | n/a | Published 2022-09-15 |
| Voxel-wise MTR change in enhancing lesions | https://doi.org/10.1002/ana.21302 | The classic trial-group method: fraction of lesion volume with significant MTR increase or decrease. | Yes, in the paper. | Scan-rescan error only. No code released. | n/a | Published 2008 |
| MTsat and g-ratio scripts from an early-MS cohort | https://doi.org/10.7488/ds/2965 | Matlab scripts for MTsat and MTR maps; lesion and normal-appearing white matter means at baseline and one year. | Lesion-mask averages, not per-lesion tracking. | In-silico g-ratio check; healthy test-retest. | Not checked | Paper 2022-10-13 |
| GitHub searches | n/a | "MTR lesion multiple sclerosis", "magnetization transfer multiple sclerosis", "multiple sclerosis lesion longitudinal myelin", "myelin phantom MRI", "lesion simulation synthetic" | n/a | n/a | n/a | All returned 0 repositories on 2026-11-23 |

Known-answer resources and datasets:

| Name | Link | What it holds | Use as a known answer | Licence | Last activity | What it lacks |
|---|---|---|---|---|---|---|
| Marmoset EAE serial MRI with histology (eLife) | https://doi.org/10.7554/eLife.73786 | Serial 7 T MRI of 6 animals in NIfTI plus myelin and microglia stains; 31 lesions classified by histology. MRI was 100% sensitive and 90% specific for remyelination. | Yes. The only open serial-MRI dataset found with a histological remyelination label per lesion. | CC0 | Published 2023-04-21 | Animal model, 7 T, proton-density contrast rather than MTR or MWF. |
| MIRROR test-retest myelin dataset | https://openneuro.org/datasets/ds008825 ; code https://github.com/PennLINC/mirror | 22 healthy adults scanned twice the same day: ihMT, QSM, MP2RAGE R1, T1w/T2w, relaxometry, diffusion; 27 metrics. | Gives the no-change noise floor for each metric. | CC0 (data), MIT (code) | Dataset 2026-10-05; code pushed 2026-10-06 | No patients, no lesions, no histology. |
| MR-histology validation review data | https://lazaral.github.io/Myelin-Validation-Systematic-Review/ | Per-study table of MRI-versus-myelin-histology correlations. | Literature-level reference values. | CC BY (data) | Paper 2021-04-15 | Not image data. |
| Interactive meta-analysis of MRI myelin biomarkers | https://pmc.ncbi.nlm.nih.gov/articles/PMC7647401 | 43 studies; MPF R² 0.77 and MWF R² 0.70 against histology, MTR 0.51. Spreadsheet and notebook provided. | Literature-level reference values. | Article licence not checked; repository has no licence file | Paper 2020-10-21; repository pushed 2021-01-17 | Not image data. |
| Phantom data for MWF at 0.55 T | https://zenodo.org/records/8340387 | Phantom measurements for a multi-gradient-echo MWF method. | Phantom known answer for one MWF method. | CC BY 4.0 | 2023-09-13 | One method, one field strength. |
| Open longitudinal MS lesion sets | Ljubljana two-time-point set (20 patients, CC BY, via "open_ms_data" on GitHub, pushed 2019-07-03); ISBI 2015 longitudinal archive https://www.nitrc.org/projects/longitudinal_ms ; Zenodo 10875606 (84 patients) | T1, T2, FLAIR, PD with lesion or lesion-change masks. | Lesion masks only. | CC BY or registration | 2019 to 2024 | Conventional contrasts only. No MTR, MWF or QSM. |
| OpenNeuro search | https://openneuro.org | Keyword searches for multiple sclerosis, myelin, magnetization transfer. | n/a | n/a | 2026-11-23 | No MS dataset with repeated myelin-sensitive MRI found. One cross-sectional MS dataset (ds007908, 28 subjects, 2026-08-17). |
| Request-only cohorts with repeated myelin MRI in MS | Early-MS cohort, 79 patients, MTsat at 0 and 12 months (PMC9668599); 17 patients, MPM, two sessions (PMC10176005); bexarotene trial lesional MTR dataset (see Tool C) | Longitudinal MT data in patients. | No ground truth. | By request, committee approval or data access agreement | 2022 to 2025 | Not open. |

Gap for Tool B: a tool that takes lesion masks plus co-registered myelin-metric maps at several time points, reports change per lesion, and proves itself on a synthetic or phantom case with a planted amount of recovery. The pieces around it exist; that step and its test do not. No open patient data exists to run it on.

### Tool C: individual-participant data and re-analysis code

| Trial | Registry and record date | Stated data route | Public deposit | Licence or conditions | What it lacks for our purpose |
|---|---|---|---|---|---|
| Clemastine crossover trial in chronic optic neuropathy (ReBUILD, 50 participants) | NCT02040298, updated 2025-09-17. Summary results posted. IPD sharing field empty. | Secondary papers state "Data are available upon reasonable request" (https://doi.org/10.1136/jnnp-2022-329221, 2022). | The 2023 MWF paper (https://doi.org/10.1073/pnas.2217635120) says data tables and analysis code were deposited in Dryad on 2023-04-30. The link given is a pre-publication share link; Dryad's public search returns no matching dataset on 2026-11-23. | Request to authors. | No public IPD. VEP latency per participant is not deposited anywhere found. |
| Bexarotene phase 2a (CCMR One, 52 participants) | ISRCTN14265371, last edited 2023-11-07. IPD plan "not provided at time of registration". | Paper states de-identified participant data, primary efficacy endpoint dataset, VEP dataset and lesional MTR dataset, with data dictionaries, are available to researchers on request to the chief investigator, signed data access agreement required, no end date. Primary endpoint data on the EudraCT site. Repeated in a 2025 secondary paper (https://doi.org/10.1093/braincomms/fcaf032). | None. The group web address named for the datasets now redirects to a department home page with no dataset links; the group's current site has no data page (both checked 2026-11-23). | Signed data access agreement. | Request only. Best-documented route of the four, and the only one that names a per-lesion MTR dataset. |
| Metformin plus clemastine phase 2a (CCMR Two, 70 participants) | NCT05131828, updated 2025-12-11. IPD sharing field "No". No results posted. | Protocol paper (https://doi.org/10.1186/s13063-025-09254-2, 2025-12-08, CC BY) states protocol, analysis plan, de-identified dataset for primary and secondary outcomes "with corresponding statistical codes" will be available with publication, on request to the chief investigator under a signed agreement. | None yet. Headline results presented 2025-09-26 (VEP latency difference -1.2 ms, 95% CI -2.4 to -0.1). | Signed data access agreement. | Registry and protocol paper disagree on sharing. Depends on the results paper appearing. |
| Opicinumab trials: RENEW (NCT01721161, 82), SYNERGY (NCT01864148, 419), AFFINITY (NCT03222973, 263) | Records updated 2016-06-30, 2017-05-03, 2022-04-28. Summary results posted for all three. AFFINITY protocol and analysis plan posted. IPD sharing fields empty. | Sponsor shares through Vivli (https://vivli.org/ourmember/biogen/): research proposal, independent review panel, data use agreement, secure research environment. | None. | Sponsor policy lists trials "for products and indications submitted and approved in both the United States and the European Union"; opicinumab was never approved, so these trials sit outside the default scope. The sponsor says it "will assess feasibility" for out-of-scope requests. Imaging data is generally not shared. | Access is discretionary. No download; analysis only inside the secure environment. |
| Related open item | Domperidone futility trial, table of results: https://doi.org/10.5061/dryad.3n5tb2rgf | Aggregate table only. | Yes | CC0, 2022-02-17 | Not participant-level. |

Routes named in the brief, one line each: public deposit, none for any of the four. Vivli, the sponsor route for opicinumab only, discretionary. ClinicalStudyDataRequest and YODA, not named by any of these trials or sponsors. On request to authors, the route for the clemastine, bexarotene and metformin-clemastine trials.

Open code for responder or heterogeneity-of-effect analysis: none found. GitHub repository searches for "clemastine", "opicinumab", "bexarotene multiple sclerosis", "metformin clemastine", "anti-LINGO" and "visual evoked potential multiple sclerosis" returned 0 repositories on 2026-11-23. GitHub code searches returned only text copies of papers and notes, no analysis code. The only promised code is the CCMR Two statistical code (with publication) and the analysis scripts in the unreachable Dryad deposit for the clemastine MWF paper.

## 3. Not verified

- **MS-SOLES app content.** The app address responds, but the page needs a browser to load; coverage, record count, last update and download function were not read. The OSF project was last modified 2023-10-02, which may mean the living updates stopped.
- **xlsx supplement of the 2025 Eur J Neurol review.** Its existence and size are confirmed; whether it holds the trial tables or only the search and extraction sheets was not opened.
- **Neurol Res 2025 review tables.** Paywalled; column structure and any supplement not seen.
- **MS Society UK pipeline page** (mssociety.org.uk, "explore treatments in trials"). Returned HTTP 403 to automated fetch. Not assessed. National MS Society and MS International Federation trackers: none found by search, sites not walked by hand.
- **Vivli listing of the opicinumab studies.** The Vivli study search needs a browser session; whether RENEW, SYNERGY or AFFINITY are listed was not confirmed. The out-of-scope reading above comes from the sponsor's published policy, not from a refusal.
- **Data sharing statements in the primary papers** for the clemastine trial (Lancet 2017) and the opicinumab trials (Lancet Neurology 2017 and 2019, and the AFFINITY paper). Not read; the rows above rely on registry fields, secondary papers and sponsor policy.
- **CCMR Two full results paper.** None found; the registry shows no results and the group's news page (2025-12-19) said submission was being prepared. A publication after that date may have been missed.
- **Dryad deposit for the clemastine MWF paper.** The share link resolves to Dryad's "pre-publication dataset sharing" page. Whether the files are still downloadable through it was not tested.
- **ClinicalStudyDataRequest and YODA.** Not searched directly. The statement that they do not apply rests on none of the trials or sponsors naming them.
- **Known-answer validation inside QUIT, DECAES, hMRI toolbox, QSMxT, SEPIA.** Repositories and dates are confirmed; their test suites and any phantom or simulation checks were not read. Only qMRLab's simulation tools were confirmed from its documentation.
- **Research Square preprint on longitudinal lesion visualisation with diffusion and MT metrics** (https://doi.org/10.21203/rs.3.rs-7361397/v1, 2025-08-22). Title matches Tool B closely; the page would not load, so code availability and validation are unknown. Worth a manual read.
- **Licences** of the clinical MPM pipeline, the MTsat scripts at doi 10.7488/ds/2965 and ihmt_proc were not established.
- **GSK239512 lesion-remyelination trial** (NCT01772199, completed, record updated 2016-08-16) uses a per-lesion MTR endpoint and comes from a sponsor with a formal data-request programme. Its data route was not checked.
- **Coverage limits.** GitHub and Zenodo were searched by keyword; code hosted on GitLab, institutional servers or NITRC, and code named without the obvious keywords, can be missed. Absence here means "not found by these searches", not proof of absence.

PubMed was used for article metadata; DOIs are given beside each article cited.
