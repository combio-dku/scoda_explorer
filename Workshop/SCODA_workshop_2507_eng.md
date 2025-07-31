# SCODA Practice Workshop
## Marker and Therapeutic Target Discovery Based on Single-Cell RNA-Seq Data

## Preparation
- **Personal Device:** &nbsp;&nbsp; A laptop with Wi-Fi and a web browser (Tablet PCs are technically possible but not recommended).  
- **Programming Language:** &nbsp;&nbsp; Python3 (No local installation required; we will use Google Colab).  
- **Presentation Materials:** &nbsp;&nbsp; To be distributed via email in advance.  
- **Prerequisite Knowledge:**  
  - Participants should be in the life science/medical field and have a basic understanding of where and how single-cell RNA-seq is applied.  
  - Experience with Python or R is preferred.  
  - Previous participation in single-cell RNA-seq analysis workshops is highly recommended.  
  - **Recommended Workshops:**  
    - Statistical Genetics Workshop by the Korean Society of Genomics (every July)  
    - BIML Workshop by the Korean Bioinformation Society (every February & August)  

---

## Workshop Agenda
1. &nbsp;&nbsp; Overview of single-cell RNA-seq analysis using SCODA  
2. &nbsp;&nbsp; **Practice I:** Introduction to AnnData format and basic SCANPY usage  
3. &nbsp;&nbsp; **Practice II:** SCODA case study I (Breast Cancer dataset)  
4. &nbsp;&nbsp; **Practice III:** SCODA case study II (Ulcerative Colitis dataset)  
5. &nbsp;&nbsp; **Practice IV:** KEGG Pathview generation and pathway visualization/analysis  

---

## Introduction to SCODA
- A brief introduction to SCODA will be provided during the workshop.  
- If you have time beforehand, watching the [BRIC Corporate Technology Webinar: SCODA Introduction](https://youtu.be/ajRnK3QeCWA?si=XGiIjtE07IMfZjdz) is recommended.  
- You can also review the [SCODA presentation slides](https://github.com/combio-dku/scoda_explorer/blob/main/SCODA_%EC%86%8C%EA%B0%9C_BRIC_%EA%B8%B0%EC%97%85%EA%B8%B0%EC%88%A0%EC%9B%A8%EB%B9%84%EB%82%98_%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C.pdf).

---

## Practice I: AnnData Format & SCANPY Basics

1. (Ctrl + Click) [Open this Jupyter notebook](https://colab.research.google.com/github/combio-dku/scoda_explorer/blob/main/Notebooks/scoda_practice_workshop_250727_1_basic.ipynb) in Google Colab.  
2. Click **“Connect”** in the top-right of the Colab tab to connect to the runtime (sign in with your Google account if required).  
3. Execute the code cells step by step to complete the practice.  

---

## Practice II & III: SCODA Case Studies (Breast Cancer & Ulcerative Colitis)

1. **Practice II:** (Ctrl + Click) [Open notebook](https://colab.research.google.com/github/combio-dku/scoda_explorer/blob/main/Notebooks/scoda_practice_workshop_250727_2_BC.ipynb) for the Breast Cancer dataset and follow the exercises.  
2. **Practice III:** (Ctrl + Click) [Open notebook](https://colab.research.google.com/github/combio-dku/scoda_explorer/blob/main/Notebooks/scoda_practice_workshop_250727_3_Colitis.ipynb) for the Ulcerative Colitis dataset and follow the exercises.  

---

## Practice IV: KEGG Pathview and Pathway Visualization

1. (Ctrl + Click) [Open this Jupyter notebook](https://colab.research.google.com/github/combio-dku/scoda_explorer/blob/main/Notebooks/scoda_practice_workshop_250727_4_R_kegg_pathview.ipynb) in Google Colab.  
   - **Note:** This notebook uses **R** in Colab.  
2. Connect to the Colab runtime (sign in if necessary).  
3. Execute each code cell in order. Step 0 requires installing R packages, which takes ~10–15 minutes.  

- **Reference:** [KEGG_Pathview_Gen_for_SCODA](https://github.com/combio-dku/KEGGPathviewGen4SCODA)

<div align="center">
  <img src="https://github.com/combio-dku/KEGGPathviewGen4SCODA/blob/main/images/KEGG_pathview_UC_mac.png" style="width:90%;"/>
</div>

---

## Trying Out the SCODA Pipeline

1. Download the [example dataset](https://drive.google.com/file/d/1DF_dGMSOi54eVc5_2DVxsWv71feFvgcb/view?usp=sharing).  
2. Visit the [SCODA demo page](https://mlbi-lab.net).  
3. In **Mandatory Input**:  
   1. Select **“Compressed 10x_mtx file sets + (optional) meta_data.csv”**.  
   2. Click **“Choose File”** and upload the downloaded dataset.  
   3. Set **Species** to *Human* and keep **Tumor cell Identification** as default.  
   4. Click **Submit** to start SCODA processing.  
   5. A progress window will appear; processing takes ~5–10 minutes.  
   6. Once finished, click **Download Result** to get the SCODA output.  
   7. Open the SCODA result with the provided notebooks and perform further data mining.  

- **Note:** If you do not provide an *Optional analysis config file*, SCODA automatically guesses the tissue type.  
  - Incorrect tissue selection can reduce annotation accuracy.  
  - To ensure correct analysis:  
    1. Download the [default analysis_config.py](https://github.com/combio-dku/scoda_explorer/blob/main/Workshop/analysis_config_breast.py).  
    2. Modify the `TISSUE` variable to `'Breast'`.  
    3. Upload this file in the **Optional analysis config file** field along with the dataset.  

---

## Reference Publications (SCODA Applications)

1. **Autoimmune disease (Ulcerative Colitis) study:**  
   [Integrative analysis of single-cell RNA-seq and gut microbiome metabarcoding data elucidates macrophage dysfunction in mice with DSS-induced ulcerative colitis](https://www.nature.com/articles/s42003-024-06409-w)  
2. **TNBC study:**  
   [A Retrospective View of the Triple-Negative Breast Cancer Microenvironment: Novel Markers, Interactions, and Mechanisms of Tumor-Associated Components Using Public Single-Cell RNA-Seq Datasets](https://www.mdpi.com/2072-6694/16/6/1173#)  
