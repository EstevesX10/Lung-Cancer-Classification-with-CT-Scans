<div align="center">

# PyLIDC Package Details
</div>

This file mainly focuses on the important details regarding the pylidc package which plays an important role within the feature extraction and exploration of the Project. Therefore, it is essencial to analyse the package API in order to improve the project robustness.

The [PyLIDC](https://pylidc.github.io/index.html) package is mainly composed by two classes:

- Scan Class
- Annotation Class
- Contour Class

## Index

> ADD INDEX FOR THE PAGE

## Scan Class

> The Scan model class refers to the top-level XML file from the LIDC. A scan has many pylidc.Annotation objects, which correspond to the unblindedReadNodule XML attributes for the scan.

### [Scan Class] Attributes

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

### [Annotation Class] Attributes

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
            <br/>
            Difficulty of detection.
            <br/>
            Higher values indicate easier detection.
            <br/><br/>
            <table>
                <tr>
                    <td>1</td>
                    <td>
                        <div align="center">
                            Extremely Subtle
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>
                        <div align="center">
                            Moderately Subtle
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>3</td>
                    <td>
                        <div align="center">
                            Fairly Subtle
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>4</td>
                    <td>
                        <div align="center">
                            Moderately Obvious
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>5</td>
                    <td>
                        <div align="center">
                            Obvious
                        </div>
                    </td>
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
            <br/>
            Internal composition of the nodule.
            <br/><br/>
            <table>
                <tr>
                    <td>1</td>
                    <td>
                        <div align="center">
                            Soft Tissue
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>
                        <div align="center">
                            Fluid
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>3</td>
                    <td>
                        <div align="center">
                            Fat
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>4</td>
                    <td>
                        <div align="center">
                            Moderately Obvious
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>5</td>
                    <td>
                        <div align="center">
                            Air
                        </div>
                    </td>
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
            &in; &lbrace;1, 2, 3, 4, 5, 6&rbrace;
        </div>
    </td>
    <td width="60%">
        <div align="center">
            <br/>
            Pattern of calcification, if present.
            <br/><br/>
            <table>
                <tr>
                    <td>1</td>
                    <td>
                        <div align="center">
                            Popcorn
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>
                        <div align="center">
                            Laminated
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>3</td>
                    <td>
                        <div align="center">
                            Solid
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>4</td>
                    <td>
                        <div align="center">
                            Non-central
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>5</td>
                    <td>
                        <div align="center">
                            Central
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>6</td>
                    <td>
                        <div align="center">
                            Absent
                        </div>
                    </td>
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
            <br/>
            The three-dimensional shape of the nodule in terms of its roundness.
            <br/><br/>
            <table>
                <tr>
                    <td>1</td>
                    <td>
                        <div align="center">
                            Linear
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>
                        <div align="center">
                            Ovoid/Linear
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>3</td>
                    <td>
                        <div align="center">
                            Ovoid
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>4</td>
                    <td>
                        <div align="center">
                            Ovoid/Round
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>5</td>
                    <td>
                        <div align="center">
                            Round
                        </div>
                    </td>
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
            <br/>
            Description of how well-defined the nodule margin is.
            <br/><br/>
            <table>
                <tr>
                    <td>1</td>
                    <td>
                        <div align="center">
                            Poorly Defined
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>
                        <div align="center">
                            Near Poorly Defined
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>3</td>
                    <td>
                        <div align="center">
                            Medium Margin
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>4</td>
                    <td>
                        <div align="center">
                            Near Sharp
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>5</td>
                    <td>
                        <div align="center">
                            Sharp
                        </div>
                    </td>
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
            <br/>
            The degree of lobulation ranging from none to marked.
            <br/><br/>
            <table>
                <tr>
                    <td>1</td>
                    <td>
                        <div align="center">
                            No Lobulation
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>
                        <div align="center">
                            Nearly No Lobulation
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>3</td>
                    <td>
                        <div align="center">
                            Medium Lobulation
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>4</td>
                    <td>
                        <div align="center">
                            Near Marked Lobulation
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>5</td>
                    <td>
                        <div align="center">
                            Marked Lobulation
                        </div>
                    </td>
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
            <br/>
            The extent of spiculation present.
            <br/><br/>
            <table>
                <tr>
                    <td>1</td>
                    <td>
                        <div align="center">
                            No Spiculation
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>
                        <div align="center">
                            Nearly No Spiculation
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>3</td>
                    <td>
                        <div align="center">
                            Medium Spiculation
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>4</td>
                    <td>
                        <div align="center">
                            Near Marked Spiculation
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>5</td>
                    <td>
                        <div align="center">
                            Marked Spiculation
                        </div>
                    </td>
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
            <br/>
            Radiographic solidity: internal texture (solid, ground glass, or mixed). 
            <br/><br/>
            <table>
                <tr>
                    <td>1</td>
                    <td>
                        <div align="center">
                            Non-Solid/GGO
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>
                        <div align="center">
                            Non-Solid/Mixed
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>3</td>
                    <td>
                        <div align="center">
                            Part Solid/Mixed
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>4</td>
                    <td>
                        <div align="center">
                            Solid/Mixed
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>5</td>
                    <td>
                        <div align="center">
                            Solid
                        </div>
                    </td>
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
            <br/>
            Subjective assessment of the likelihood of malignancy, assuming the scan originated from a 60-year-old male smoker.
            <br/><br/>
            <table textalign="center">
                <tr>
                    <td>1</td>
                    <td>
                        <div align="center">
                            Highly Unlikely
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>
                        <div align="center">
                            Moderately Unlikely
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>3</td>
                    <td>
                        <div align="center">
                            Indeterminate
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>4</td>
                    <td>
                        <div align="center">
                            Moderately Suspicious
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>5</td>
                    <td>
                        <div align="center">
                            Highly Suspicious
                        </div>
                    </td>
                </tr>
            </table>
        </div>
    </td>
  </tr>
</table>

## Contour Class

> The Contour class holds the nodule boundary coordinate data of a pylidc.Annotation object for a single slice in the CT volume.

### [Contour Class] Attributes

According to the Documentation an instance of [Contour](https://pylidc.github.io/contour.html) contains the following attributes:


<table width="100%" border="1" cellpadding="5">
  <tr>
    <th colspan="3" height="100%">
        <div align="center">
            Contour Class Attributes
        </div>
    </th>
  </tr>
  
  <tr>
    <td width="15%">
        <div align="center">
        <b>Parameter</b>
        </div>
    </td>
    <td width="5%">
        <div align="center">
        <b>Type</b>
        </div>
    </td>
    <td width="75%">
        <div align="center">
        <b>Description</b>
        </div>
    </td>
  </tr>

  <tr>
    <td width="15%">
        <div align="center">
        <b>inclusion</b>
        </div>
    </td>
    <td width="5%">
        <div align="center">
            bool
        </div>
    </td>
    <td width="75%">
        <div align="center">
            If True, the area inside the contour is included as part of the nodule. If False, the area inside the contour is excluded from the nodule
        </div>
    </td>
  </tr>

  <tr>
    <td width="15%">
        <div align="center">
        <b>image_z_position</b>
        </div>
    </td>
    <td width="5%">
        <div align="center">
            float
        </div>
    </td>
    <td width="75%">
        <div align="center">
            This is the imageZposition defined via the xml annnotations for this contour. It is the z-coordinate of DICOM attribute (0020,0032)
        </div>
    </td>
  </tr>

  <tr>
    <td width="15%">
        <div align="center">
        <b>dicom_file_name</b>
        </div>
    </td>
    <td width="5%">
        <div align="center">
            string
        </div>
    </td>
    <td width="75%">
        <div align="center">
            This is the name of the corresponding DICOM file for the scan to which this contour belongs, having the same image_z_position
        </div>
    </td>
  </tr>

  <tr>
    <td width="15%">
        <div align="center">
        <b>coords</b>
        </div>
    </td>
    <td width="5%">
        <div align="center">
            string
        </div>
    </td>
    <td width="75%">
        <div align="center">
            These are the sequential (x,y) coordinates of the curve, stored as a string. It is better to access these coordinates using the to_matrix method, which returns a numpy array rather than a string
        </div>
    </td>
  </tr>

  <tr>
    <td width="15%">
        <div align="center">
        <b>image_k_position</b>
        </div>
    </td>
    <td width="5%">
        <div align="center">
            float
        </div>
    </td>
    <td width="75%">
        <div align="center">
            Similar to Contour.image_z_position, but returns the index instead of the z coordinate value
        </div>
    </td>
  </tr>
</table>

### [Contour Class] Methods

According to the Documentation an instance of [Contour](https://pylidc.github.io/contour.html) contains the following Method:

<table width="100%" border="1" cellpadding="5">
  <tr>
    <th colspan="3" height="100%">
        <div align="center">
            Contour Class Method
        </div>
    </th>
  </tr>

  <tr>
    <td width="15%">
        <div align="center">
        <b>Method</b>
        </div>
    </td>
    <td width="55%">
        <div align="center">
        <b>Arguments</b>
        </div>
    </td>
    <td width="30%">
        <div align="center">
        <b>Description</b>
        </div>
    </td>
  </tr>

  <tr>
    <td width="15%">
        <div align="center">
        <b>to_matrix</b>
        </div>
    </td>
    <td width="55%">
        <div align="center">
            include_k (bool, default = True)
            <br/>
            Set include_k = False to omit the k axis coordinate.
        </div>
    </td>
    <td width="30%">
        <div align="center">
            Return the contour-annotation coordinates as a matrix where each row contains an (i,j,k) index coordinate into the image volume.
        </div>
    </td>
  </tr>
</table>

### [Contour Class] Code Snippets

<div align="right">

> Plot a contour on top of the image volume
</div>

```python 
import pylidc as pl
import matplotlib.pyplot as plt

ann = pl.query(pl.Annotation).first()
vol = ann.scan.to_volume()
con = ann.contours[3]

k = con.image_k_position
ii,jj = ann.contours[3].to_matrix(include_k=False).T

plt.imshow(vol[:,:,46], cmap=plt.cm.gray)
plt.plot(jj, ii, '-r', lw=1, label="Nodule Boundary")
plt.legend()
plt.show()
```

