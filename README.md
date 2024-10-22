<div align="center">

# Labs AI & DS | Lung Cancer Classification with CT Scans
</div>

<p align="center" width="100%">
    <img src="./Lung Cancer Classification with CT Scans/Assets/LungCancerDetection.png" width="55%" height="55%" />
</p>

<div align="center">
    <a>
        <img src="https://img.shields.io/badge/Made%20with-Python-b62d46?style=for-the-badge&logo=Python&logoColor=b62d46">
    </a>
    <a>
        <img src="https://img.shields.io/badge/Made%20with-Jupyter-b62d46?style=for-the-badge&logo=Jupyter&logoColor=b62d46">
    </a>
</div>

<br/>

<div align="center">
    <a href="https://github.com/EstevesX10/Lung-Cancer-Classification-with-CT-Scans/blob/main/LICENSE">
        <img src="https://img.shields.io/github/license/EstevesX10/Lung-Cancer-Classification-with-CT-Scans?style=flat&logo=gitbook&logoColor=b62d46&label=License&color=b62d46">
    </a>
    <a href="">
        <img src="https://img.shields.io/github/repo-size/EstevesX10/Lung-Cancer-Classification-with-CT-Scans?style=flat&logo=googlecloudstorage&logoColor=b62d46&logoSize=auto&label=Repository%20Size&color=b62d46">
    </a>
    <a href="">
        <img src="https://img.shields.io/github/stars/EstevesX10/Lung-Cancer-Classification-with-CT-Scans?style=flat&logo=adafruit&logoColor=b62d46&logoSize=auto&label=Stars&color=b62d46">
    </a>
    <a href="https://github.com/EstevesX10/Lung-Cancer-Classification-with-CT-Scans/blob/main/DEPENDENCIES.md">
        <img src="https://img.shields.io/badge/Dependencies-DEPENDENCIES.md-white?style=flat&logo=anaconda&logoColor=b62d46&logoSize=auto&color=b62d46"> 
    </a>
</div>

## Project Overview

``Lung cancer`` remains the leading cause of **cancer-related mortality worldwide**. Unfortunately, only 16% of cases are diagnosed at an **early**, localized stage, where patients have a **five-year survival rate exceeding 50%**. When lung cancer is identified at more **advanced stages**, the survival rate plummets to just **5%**.

Given this stark difference, ``early diagnosis is critical`` for improving patient outcomes. Non-invasive imaging methods, such as **computed tomography (CT)**, have proven effective in providing crucial information regarding tumor status. This opens opportunities for developing **computer-aided diagnosis (CAD) systems** capable of assessing the malignancy risk of lung nodules and **supporting clinical decision-making**.

The goal of this project is to create a **machine learning-based solution for classifying lung nodules as benign or malignant using CT images** available within **LIDC-IDRI dataset**.

## Project Development

### Dependencies & Execution

As a request from ou professor this project was developed using a `Notebook`. Therefore if you're looking forward to test it out yourself, keep in mind to either use a **[Anaconda Distribution](https://www.anaconda.com/)** or a 3rd party software that helps you inspect and execute it. 

Therefore, for more informations regarding the **Virtual Environment** used in Anaconda, consider checking the [DEPENDENCIES.md](https://github.com/EstevesX10/Lung-Cancer-Classification-with-CT-Scans/blob/main/DEPENDENCIES.md) file.

### Planned Work

The project will involve several ``key phases``, including:

- ``Data Preprocessing`` : **Cleaning and preparing the CT scan data** to ensure its quality and consistency for further analysis.
- ``Feature Engineering`` : Leveraging **radiomics** to extract meaningful **features** from the scans.
- ``Model Development and Evaluation`` : **Training and fine-tuning machine learning models** to accurately classify lung nodules based on their malignancy status. It also focuses on assessing **model performance** using key metrics such as **balanced accuracy** and **AUC**, and validating results through robust methods such as **k-fold cross-validation**.
- ``Statistical Inference`` : Conduct a statistical analysis to determine **performance differences between the models** and identify which one delivers the best results for this classification task.
  
The ultimate objective of this automated classification system is to ``aid in clinical decision-making``, offering a supplementary screening tool that **reduces the workload on radiologists** while improving early detection rates for lung cancer.

### Datasets

If you're interested in trying this project yourself, you'll need access to the ``complete datasets`` we've created. Since GitHub has **file size limits**, we've made them all available [here](https://drive.google.com/drive/folders/1X9DI72QTb86kFYYeuGSrktsM3eE1_pVt?usp=drive_link).

## Project Results

### [Initial] Target Class Distribution

Here’s a quick overview of how the ``nodular malignancy`` in the dataset is **distributed across five different levels of malignancy**.

<br/>

<div align="center">
    <img src="./Lung Cancer Classification with CT Scans/ExperimentalResults/DataEvaluation/InitialTargetDistribution.png" width="80%" height="80%" />
</div>

### Machine Learning Models Evaluation

Here are some of the results obtained from various ``selected machine learning algorithms``, which we found to be the most interesting based on their **balanced accuracy scores**.

<table width="100%">
  <tr>
    <th colspan="2" height="100%">
        <div align="center">
            Performance Evaluation
        </div>
    </th>
  </tr>

  <tr>
    <td width="30%">
        <div align="center">
        <b>Algorithm</b>
        </div>
    </td>
    <td width="70%">
        <div align="center">
        <b>Metrics</b>
        </div>
    </td>
  </tr>

  <tr>
    <td width="30%">
        <div align="center">
        <b>SVM</b>
        </div>
    </td>
    <td width="70%">
        <p align="center"><img src="./Lung Cancer Classification with CT Scans/ExperimentalResults/SVM/balanced_accuracy/evaluationPlot.png"/>
        </p>
    </td>
  </tr>

  <tr>
    <td width="30%">
        <div align="center">
        <b>Random Forest</b>
        </div>
    </td>
    <td width="70%">
        <p align="center"><img src="./Lung Cancer Classification with CT Scans/ExperimentalResults/RandomForest/balanced_accuracy/evaluationPlot.png"/>
        </p>
    </td>
  </tr>

  <tr>
    <td width="30%">
        <div align="center">
        <b>XGBoost</b>
        </div>
    </td>
    <td width="70%">
        <p align="center"><img src="./Lung Cancer Classification with CT Scans/ExperimentalResults/XGBoost/balanced_accuracy/evaluationPlot.png"/>
        </p>
    </td>
  </tr>

  <tr>
    <td width="30%">
        <div align="center">
        <b>Voting Classifier</b>
        </div>
    </td>
    <td width="70%">
        <p align="center"><img src="./Lung Cancer Classification with CT Scans/ExperimentalResults/VotingClassifier/balanced_accuracy/evaluationPlot.png"/>
        </p>
    </td>
  </tr>
</table>

### Critical Differences Diagram

To better illustrate the **performance differences** between the models, let's examine their respective ``critical differences diagram``.

<br/>

<div align="center">
    <img src="./Lung Cancer Classification with CT Scans/ExperimentalResults/DataEvaluation/CriticalDifferencesDiagram.png" width="70%" height="80%" />
</div>

<br/>

In this diagram, **XGBoost and the Voting Classifier share the same rank (2.2)**, suggesting that they **performed similarly and may be the most suited for providing a solution to the classification problem**.

## Authorship

- **Authors** &#8594; [Francisco Macieira](https://github.com/franciscovmacieira), [Gonçalo Esteves](https://github.com/EstevesX10) and [Nuno Gomes](https://github.com/NightF0x26)
- **Course** &#8594; Laboratory AI and DS [CC3044]
- **University** &#8594; Faculty of Sciences, University of Porto
 
<div align="right">
<sub>

<!-- <sup></sup> -->
`README.md by Gonçalo Esteves`
</sub>
</div>