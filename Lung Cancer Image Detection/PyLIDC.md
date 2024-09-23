<div align="center">

# PyLIDC Package Details
</div>

This file mainly focuses on the important details regarding the pylidc package which plays an important role within the feature extraction and exploration of the Project. Therefore, it is essencial to analyse the package API in order to improve the project robustness.

The [PyLIDC](https://pylidc.github.io/index.html) package is mainly composed by two classes:

- Scan Class
- Annotation Class

## Scan Class

> The Scan model class refers to the top-level XML file from the LIDC. A scan has many pylidc.Annotation objects, which correspond to the unblindedReadNodule XML attributes for the scan.

According to the Documentation an instance of the [Scan](https://pylidc.github.io/scan.html) contains the following attributes:

<table width="100%" border="1" cellpadding="5">
  <tr>
    <th colspan="3" height="100%">
        <div align="center">
            Scan Class Attributes
        </div>
    </th>
  </tr>
  
  <tr>
    <td width="25%">
        <div align="center">
        <b>Parameter</b>
        </div>
    </td>
    <td width="25%">
        <div align="center">
        <b>Type</b>
        </div>
    </td>
    <td width="25%">
        <div align="center">
        <b>Description</b>
        </div>
    </td>
  </tr>

  <tr>
    <td width="15%">
        <div align="center">
        <b>study_instance_uid</b>
        </div>
    </td>
    <td width="5%">
        <div align="center">
            string
        </div>
    </td>
    <td width="75%">
        <div align="center">
            DICOM attribute (0020,000D)
        </div>
    </td>
  </tr>

  <tr>
    <td width="15%">
        <div align="center">
        <b>series_instance_uid </b>
        </div>
    </td>
    <td width="5%">
        <div align="center">
            string
        </div>
    </td>
    <td width="75%">
        <div align="center">
            DICOM attribute (0020,000E)
        </div>
    </td>
  </tr>

  <tr>
    <td width="15%">
        <div align="center">
        <b>patient_id </b>
        </div>
    </td>
    <td width="5%">
        <div align="center">
            string
        </div>
    </td>
    <td width="75%">
        <div align="center">
            Identifier of the form “LIDC-IDRI-dddd” where dddd is a string of integers
        </div>
    </td>
  </tr>

  <tr>
    <td width="15%">
        <div align="center">
        <b>slice_thickness </b>
        </div>
    </td>
    <td width="5%">
        <div align="center">
            float
        </div>
    </td>
    <td width="75%">
        <div align="center">
            DICOM attribute (0018,0050). Note that this may not be equal to the slice_spacing attribute (see below)
        </div>
    </td>
  </tr>

  <tr>
    <td width="15%">
        <div align="center">
        <b>slice_zvals</b>
        </div>
    </td>
    <td width="5%">
        <div align="center">
            ndarray
        </div>
    </td>
    <td width="75%">
        <div align="center">
            The “z-values” for the slices of the scan (i.e., the last coordinate of the ImagePositionPatient DICOM attribute) as a NumPy array sorted in increasing order
        </div>
    </td>
  </tr>

  <tr>
    <td width="15%">
        <div align="center">
        <b>slice_spacing</b>
        </div>
    </td>
    <td width="5%">
        <div align="center">
            float
        </div>
    </td>
    <td width="75%">
        <div align="center">
            This computed property is the median of the difference between the slice coordinates, i.e., scan.slice_zvals
        </div>
    </td>
  </tr>

  <tr>
    <td width="15%">
        <div align="center">
        <b>pixel_spacing</b>
        </div>
    </td>
    <td width="5%">
        <div align="center">
            float
        </div>
    </td>
    <td width="75%">
        <div align="center">
            Dicom attribute (0028,0030). This is normally two values. All scans in the LIDC have equal resolutions in the transverse plane, so only one value is used here    
        </div>
    </td>
  </tr>

  <tr>
    <td width="15%">
        <div align="center">
        <b>contrast_used</b>
        </div>
    </td>
    <td width="5%">
        <div align="center">
            bool
        </div>
    </td>
    <td width="75%">
        <div align="center">
            If the DICOM file for the scan had any Contrast tag, this is marked as True   
        </div>
    </td>
  </tr>

  <tr>
    <td width="15%">
        <div align="center">
        <b>is_from_initial</b>
        </div>
    </td>
    <td width="5%">
        <div align="center">
            bool
        </div>
    </td>
    <td width="75%">
        <div align="center">
            Indicates whether or not this PatientID was tagged as part of the initial 399 release 
        </div>
    </td>
  </tr>

  <tr>
    <td width="15%">
        <div align="center">
        <b>sorted_dicom_file_names</b>
        </div>
    </td>
    <td width="5%">
        <div align="center">
            string
        </div>
    </td>
    <td width="75%">
        <div align="center">
            This attribute is no longer used, and can be ignored 
        </div>
    </td>
  </tr>
</table>

## Annotation Class

> The Nodule model class holds the information from a single physicians annotation of a nodule >= 3mm class with a particular scan. A nodule has many contours, each of which refers to the contour drawn for nodule in each scan slice.

According to the Documentation an instance of [Annotation](https://pylidc.github.io/annotation.html) contains the following attributes:

<table width="100%" border="1" cellpadding="5">
  <tr>
    <th colspan="4" height="100%">
        <div align="center">
            Annotation Class Attributes
        </div>
    </th>
  </tr>
  
  <tr>
    <td width="5%">
        <div align="center">
        <b>Parameter</b>
        </div>
    </td>
    <td width="5%">
        <div align="center">
        <b>Type</b>
        </div>
    </td>
    <td width="30%">
        <div align="center">
        <b>Range</b>
        </div>
    </td>
    <td width="60%">
        <div align="center">
        <b>Description</b>
        </div>
    </td>
  </tr>

  <tr>
    <td width="5%">
        <div align="center">
        <b>subtlety</b>
        </div>
    </td>
    <td width="5%">
        <div align="center">
            Integer
        </div>
    </td>
    <td width="30%">
        <div align="center">
            &in; &lbrace;1, 2, 3, 4, 5&rbrace;
        </div>
    </td>
    <td width="60%">
        <div align="center">
            Difficulty of detection.
            <br/>
            Higher values indicate easier detection.
            <br/><br/>
            <table style="text-align:center">
                <tr>
                    <td>1</td>
                    <td>Extremely Subtle</td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>Moderately Subtle</td>
                </tr>
                <tr>
                    <td>3</td>
                    <td>Fairly Subtle</td>
                </tr>
                <tr>
                    <td>4</td>
                    <td>Moderately Obvious</td>
                </tr>
                <tr>
                    <td>5</td>
                    <td>Obvious</td>
                </tr>
            </table>
        </div>
    </td>
  </tr>

  <tr>
    <td width="5%">
        <div align="center">
        <b>internalStructure</b>
        </div>
    </td>
    <td width="5%">
        <div align="center">
            Integer
        </div>
    </td>
    <td width="30%">
        <div align="center">
            &in; &lbrace;1, 2, 3, 4, 5&rbrace;
        </div>
    </td>
    <td width="60%">
        <div align="center">
            Internal composition of the nodule.
            <br/><br/>
            <table>
                <tr>
                    <td>1</td>
                    <td>Soft Tissue</td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>Fluid</td>
                </tr>
                <tr>
                    <td>3</td>
                    <td>Fat</td>
                </tr>
                <tr>
                    <td>4</td>
                    <td>Moderately Obvious</td>
                </tr>
                <tr>
                    <td>5</td>
                    <td>Air</td>
                </tr>
            </table>
        </div>
    </td>
  </tr>

  <tr>
    <td width="5%">
        <div align="center">
        <b>calcification</b>
        </div>
    </td>
    <td width="5%">
        <div align="center">
            Integer
        </div>
    </td>
    <td width="30%">
        <div align="center">
            &in; &lbrace;1, 2, 3, 4, 5, 6 &rbrace;
        </div>
    </td>
    <td width="60%">
        <div align="center">
            Pattern of calcification, if present.
            <br/><br/>
            <table>
                <tr>
                    <td>1</td>
                    <td>Popcorn</td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>Laminated</td>
                </tr>
                <tr>
                    <td>3</td>
                    <td>Solid</td>
                </tr>
                <tr>
                    <td>4</td>
                    <td>Non-central</td>
                </tr>
                <tr>
                    <td>5</td>
                    <td>Central</td>
                </tr>
                <tr>
                    <td>6</td>
                    <td>Absent</td>
                </tr>
            </table>
        </div>
    </td>
  </tr>

  <tr>
    <td width="5%">
        <div align="center">
        <b>sphericity</b>
        </div>
    </td>
    <td width="5%">
        <div align="center">
            Integer
        </div>
    </td>
    <td width="30%">
        <div align="center">
            &in; &lbrace;1, 2, 3, 4, 5&rbrace;
        </div>
    </td>
    <td width="60%">
        <div align="center">
            The three-dimensional shape of the nodule in terms of its roundness.
            <br/><br/>
            <table>
                <tr>
                    <td>1</td>
                    <td>Linear</td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>Ovoid/Linear</td>
                </tr>
                <tr>
                    <td>3</td>
                    <td>Ovoid</td>
                </tr>
                <tr>
                    <td>4</td>
                    <td>Ovoid/Round</td>
                </tr>
                <tr>
                    <td>5</td>
                    <td>Round</td>
                </tr>
            </table>
        </div>
    </td>
  </tr>

  <tr>
    <td width="5%">
        <div align="center">
        <b>margin</b>
        </div>
    </td>
    <td width="5%">
        <div align="center">
            Integer
        </div>
    </td>
    <td width="30%">
        <div align="center">
            &in; &lbrace;1, 2, 3, 4, 5&rbrace;
        </div>
    </td>
    <td width="60%">
        <div align="center">
            Description of how well-defined the nodule margin is.
            <br/><br/>
            <table>
                <tr>
                    <td>1</td>
                    <td>Poorly Defined</td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>Near Poorly Defined</td>
                </tr>
                <tr>
                    <td>3</td>
                    <td>Medium Margin</td>
                </tr>
                <tr>
                    <td>4</td>
                    <td>Near Sharp</td>
                </tr>
                <tr>
                    <td>5</td>
                    <td>Sharp</td>
                </tr>
            </table>
        </div>
    </td>
  </tr>

  <tr>
    <td width="5%">
        <div align="center">
        <b>lobulation</b>
        </div>
    </td>
    <td width="5%">
        <div align="center">
            Integer
        </div>
    </td>
    <td width="30%">
        <div align="center">
            &in; &lbrace;1, 2, 3, 4, 5&rbrace;
        </div>
    </td>
    <td width="60%">
        <div align="center">
            The degree of lobulation ranging from none to marked.
            <br/><br/>
            <table>
                <tr>
                    <td>1</td>
                    <td>No Lobulation</td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>Nearly No Lobulation</td>
                </tr>
                <tr>
                    <td>3</td>
                    <td>Medium Lobulation</td>
                </tr>
                <tr>
                    <td>4</td>
                    <td>Near Marked Lobulation</td>
                </tr>
                <tr>
                    <td>5</td>
                    <td>Marked Lobulation</td>
                </tr>
            </table>
        </div>
    </td>
  </tr>

  <tr>
    <td width="5%">
        <div align="center">
        <b>spiculation</b>
        </div>
    </td>
    <td width="5%">
        <div align="center">
            Integer
        </div>
    </td>
    <td width="30%">
        <div align="center">
            &in; &lbrace;1, 2, 3, 4, 5&rbrace;
        </div>
    </td>
    <td width="60%">
        <div align="center">
            The extent of spiculation present.
            <br/><br/>
            <table>
                <tr>
                    <td>1</td>
                    <td>No Spiculation</td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>Nearly No Spiculation</td>
                </tr>
                <tr>
                    <td>3</td>
                    <td>Medium Spiculation</td>
                </tr>
                <tr>
                    <td>4</td>
                    <td>Near Marked Spiculation</td>
                </tr>
                <tr>
                    <td>5</td>
                    <td>Marked Spiculation</td>
                </tr>
            </table>
        </div>
    </td>
  </tr>

  <tr>
    <td width="5%">
        <div align="center">
        <b>texture</b>
        </div>
    </td>
    <td width="5%">
        <div align="center">
            Integer
        </div>
    </td>
    <td width="30%">
        <div align="center">
            &in; &lbrace;1, 2, 3, 4, 5&rbrace;
        </div>
    </td>
    <td width="60%">
        <div align="center">
            Radiographic solidity: internal texture (solid, ground glass, or mixed). 
            <br/><br/>
            <table>
                <tr>
                    <td>1</td>
                    <td>Non-Solid/GGO</td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>Non-Solid/Mixed</td>
                </tr>
                <tr>
                    <td>3</td>
                    <td>Part Solid/Mixed</td>
                </tr>
                <tr>
                    <td>4</td>
                    <td>Solid/Mixed</td>
                </tr>
                <tr>
                    <td>5</td>
                    <td>Solid</td>
                </tr>
            </table>
        </div>
    </td>
  </tr>

  <tr>
    <td width="5%">
        <div align="center">
        <b>malignancy</b>
        </div>
    </td>
    <td width="5%">
        <div align="center">
            Integer
        </div>
    </td>
    <td width="30%">
        <div align="center">
            &in; &lbrace;1, 2, 3, 4, 5&rbrace;
        </div>
    </td>
    <td width="60%">
        <div align="center">
            Subjective assessment of the likelihood of malignancy, assuming the scan originated from a 60-year-old male smoker.
            <br/><br/>
            <table textalign="center">
                <tr>
                    <td>1</td>
                    <td>Highly Unlikely</td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>Moderately Unlikely</td>
                </tr>
                <tr>
                    <td>3</td>
                    <td>Indeterminate</td>
                </tr>
                <tr>
                    <td>4</td>
                    <td>Moderately Suspicious</td>
                </tr>
                <tr>
                    <td>5</td>
                    <td>Highly Suspicious</td>
                </tr>
            </table>
        </div>
    </td>
  </tr>
</table>