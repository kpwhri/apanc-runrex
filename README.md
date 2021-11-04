





<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div>
  <p>
    <a href="https://github.com/kpwhri/apanc-runrex">
      <img src="images/logo.png" alt="Logo">
    </a>
  </p>

  <h3 align="center">Acute Pancreatitis Runrex</h3>

  <p>
    Feature extraction for developing an algorithm to identify acute pancreatitis cases.
    Additional steps will require use of these variables to build a predictive algorithm.
  </p>
</div>


<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* Python 3.8+
* runrex package: https://github.com/kpwhri/runrex

### Installation
 
1. Clone the repo
```sh
git clone https://github.com/kpwhri/apanc-runrex.git
```
2. Install requirements
```sh
pip install -r requirements.txt -r requirements-dev.txt
```
3. Run tests.
```sh
set/export PYTHONPATH=src
pytest tests
```


<!-- USAGE EXAMPLES -->
## Usage

* Build a configuration file as defined in [runrex](https://github.com/kpwhri/runrex)
    - Full details defined in that project's [schema.py](https://github.com/kpwhri/runrex/blob/master/src/runrex/schema.py)
* `python run.py runrex.conf.(py|json|yaml)`


## Variables Identified

Variables (called 'algorithms') are broken down into various 'categories'. Either can be used in building features.

|Algorithm|Category|Description|
|---|---|---|
|[pain](src/apanc_nlp/algo/pain.py)|ABD_PAIN|Abdominal pain|
|[pain](src/apanc_nlp/algo/pain.py)|RADIATING_TO_BACK|Pain described as radiating to the back|
|[pain](src/apanc_nlp/algo/pain.py)|ACUTE|Acute pain|
|[pain](src/apanc_nlp/algo/pain.py)|EPIGASTRIC|Epigastric pain|
|[pain](src/apanc_nlp/algo/pain.py)|CHEST|Chest pain|
|[pain](src/apanc_nlp/algo/pain.py)|CHRONIC|Chronic Pain|
|[pain](src/apanc_nlp/algo/pain.py)|RECENT|Recent pain (in weeks)|
|[pain](src/apanc_nlp/algo/pain.py)|VERY_RECENT|Recent pain (in days)|
|[pain](src/apanc_nlp/algo/pain.py)|LONG_AGO|Non-recent pain (in months)|
|[pain](src/apanc_nlp/algo/pain.py)|SUDDEN_ONSET|Sudden onset pain|
|[pain](src/apanc_nlp/algo/pain.py)|WORSENING|Pain described as worsening|
|[pain](src/apanc_nlp/algo/pain.py)|UNKNOWN_DURATION|Likely unrecognized time format for recency|
|[pancreatitis](src/apanc_nlp/algo/pancreatitis.py)|POSITIVE|Generic pancreatitis|
|[pancreatitis](src/apanc_nlp/algo/pancreatitis.py)|ACUTE|Acute pancreatitis|
|[pancreatitis](src/apanc_nlp/algo/pancreatitis.py)|CHRONIC|Chronic pancreatitis|
|[pancreatitis](src/apanc_nlp/algo/pancreatitis.py)|INFLAMMATION|inflammation|
|[pancreatitis](src/apanc_nlp/algo/pancreatitis.py)|INTERSTITIAL|interstitial pancreatitis|
|[pancreatitis](src/apanc_nlp/algo/pancreatitis.py)|PERI_INFLAMMATION|Peri-inflammation|
|[pancreatitis](src/apanc_nlp/algo/pancreatitis.py)|CONSISTENT_WITH|Radiology conclusion-like language (e.g., consistent with)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|ACUTE_APPENDICITIS|Presence of acute_appendicitis (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|GALL_BLADDER_DISEASE|Presence of gall_bladder_disease (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|BOWEL_MOVEMENTS|Presence of bowel_movements (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|COLANGITIS|Presence of colangitis (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|CHRONIC_PAIN|Presence of chronic_pain (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|STROKE|Presence of stroke (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|BLOOD_IN_STOOL|Presence of blood_in_stool (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|BLOOD_IN_VOMIT|Presence of blood_in_vomit (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|PEPTIC_ULCER|Presence of peptic_ulcer (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|GASTRODUODENITIS|Presence of gastroduodenitis (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|GERD|Presence of gerd (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|INTESTINAL_OBSTRUCTION|Presence of intestinal_obstruction (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|ILEUS|Presence of ileus (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|CONSTIPATION|Presence of constipation (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|MESENTERIC_ISCHEMIA|Presence of mesenteric_ischemia (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|DIVERTICULOSIS|Presence of diverticulosis (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|APPENDICITIS|Presence of appendicitis (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|HEPATITIS|Presence of hepatitis (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|INFLUENZA|Presence of influenza (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|FOOD_POISONING|Presence of food_poisoning (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|ASCITES|Presence of ascites (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|NEPHROLITHIASIS|Presence of nephrolithiasis (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|DKA|Presence of dka (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|MYOCARDIAL_ISCHEMIA|Presence of myocardial_ischemia (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|BILIARY_CANCER|Presence of biliary_cancer (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|IBD|Presence of ibd (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|INFECTIOUS_GE|Presence of infectious_ge (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|ESOPHAGITIS|Presence of esophagitis (competing diagnosis)|
|[competing_dx](src/apanc_nlp/algo/competing_dx.py)|NEGATIVE|Presence of negative (competing diagnosis)|
|[fluid](src/apanc_nlp/algo/fluid.py)|APFC|Acute peri-pancreatic fluid|
|[fluid](src/apanc_nlp/algo/fluid.py)|PANCREATIC|Pancreatic fluid|
|[fluid](src/apanc_nlp/algo/fluid.py)|WALLED_OFF|Walled off fluid|
|[nausea](src/apanc_nlp/algo/nausea.py)|VOMITING|Vomiting|
|[nausea](src/apanc_nlp/algo/nausea.py)|NAUSEA|Nausea|
|[necrosis](src/apanc_nlp/algo/necrosis.py)|POSITIVE|Generic mention of necrosis|
|[necrosis](src/apanc_nlp/algo/necrosis.py)|PANCREATITIS|Pancreatic necrosis|
|[necrosis](src/apanc_nlp/algo/necrosis.py)|PERIPANCREATIC|Peri-pancreatic necrosis|
|[necrosis](src/apanc_nlp/algo/necrosis.py)|ACUTE_COLLECTION|Acute necrotic collection|
|[pseudocyst](src/apanc_nlp/algo/pseudocyst.py)|POSITIVE|Generic pseudocyst|
|[pseudocyst](src/apanc_nlp/algo/pseudocyst.py)|PANCREATIC|Pancreatic pseudocyst|

## Output Format

Recommended format is `jsonl`. For more details, see [runrex](https://github.com/kpwhri/runrex).


## Versions

<!-- Uses [SEMVER](https://semver.org/). -->

Updates/changes are not expected. Versioning likely based on release timing in `YYYYmm`. See https://github.com/kpwhri/apanc-runrex/releases.

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/kpwhri/apanc-runrex/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` or https://kpwhri.mit-license.org for more information.



<!-- CONTACT -->
## Contact

Please use the [issue tracker](https://github.com/kpwhri/apanc-runrex/issues). 


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* This work was funded as part of the [Sentinel Initiative](https://www.fda.gov/safety/fdas-sentinel-initiative).





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/kpwhri/apanc-runrex.svg?style=flat-square
[contributors-url]: https://github.com/kpwhri/apanc-runrex/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/kpwhri/apanc-runrex.svg?style=flat-square
[forks-url]: https://github.com/kpwhri/apanc-runrex/network/members
[stars-shield]: https://img.shields.io/github/stars/kpwhri/apanc-runrex.svg?style=flat-square
[stars-url]: https://github.com/kpwhri/apanc-runrex/stargazers
[issues-shield]: https://img.shields.io/github/issues/kpwhri/apanc-runrex.svg?style=flat-square
[issues-url]: https://github.com/kpwhri/apanc-runrex/issues
[license-shield]: https://img.shields.io/github/license/kpwhri/apanc-runrex.svg?style=flat-square
[license-url]: https://kpwhri.mit-license.org/
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/company/kaiser-permanente-washington
<!-- [product-screenshot]: images/screenshot.png -->