<div align="center">

# PyLIDC Package Details
</div>

This file mainly focuses on the important details regarding the pylidc package which plays an important role within the feature extraction and exploration of the Project. Therefore, it is essencial to analyse the package API in order to improve the project robustness.

The [PyLIDC](https://pylidc.github.io/index.html) package is mainly composed by the following classes:

- Scan Class
- Annotation Class
- Contour Class

## Documentation Index

Below is a simple index to help you navigate through the package documentation:

### 📁 [Scan Class](#scan-class)
- 📋 [Attributes](#scan-class-attributes)
- ⚙️ [Methods](#scan-class-methods)
- 💡 [Code Snippets](#scan-class-code-snippets)

### 📁 [Annotation Class](#annotation-class)
- 📋 [Attributes](#annotation-class-attributes)
- ⚙️ [Methods](#annotation-class-methods)
- 💡 [Code Snippets](#annotation-class-code-snippets)

### 📁 [Contour Class](#contour-class)
- 📋 [Attributes](#contour-class-attributes)
- ⚙️ [Methods](#contour-class-methods)
- 💡 [Code Snippets](#contour-class-code-snippets)

## Scan Class

> The Scan model class refers to the top-level XML file from the LIDC. A scan has many pylidc.Annotation objects, which correspond to the unblindedReadNodule XML attributes for the scan.

### [Scan Class] Attributes

According to the Documentation an instance of the [Scan](https://pylidc.github.io/scan.html) contains the following Attributes:

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
            This computes the median of the difference between the slice coordinates
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
</table>

### [Scan Class] Methods

According to the Documentation an instance of the [Scan](https://pylidc.github.io/scan.html) contains the following Methods:

<table width="100%" border="1" cellpadding="5">
  <tr>
    <th colspan="3" height="100%">
        <div align="center">
            Scan Class Methods
        </div>
    </th>
  </tr>
  
  <tr>
    <td width="5%">
        <div align="center">
        <b>Method</b>
        </div>
    </td>
    <td width="65%">
        <div align="center">
        <b>Arguments</b>
        </div>
    </td>
    <td width="30%">
        <div align="center">
        <b>Returns</b>
        </div>
    </td>
  </tr>

  <tr>
    <td width="5%">
        <div align="center">
        <b>cluster_annotations()</b>
        </div>
    </td>
    <td width="65%">
        <div align="center">
            <b>metric</b><br/>(string or callable, default 'min')
            <br/><br/>
            If string, checks for available metrics. If callable, the provided function, should take two Annotation objects and return a float
            <hr/>
            <b>tol</b><br/>(float, default=None)
            <br/><br/>
            A distance in millimeters. Annotations are grouped when the minimum distance between their boundary contour points is less than tol
            <hr/>
            <b>factor</b><br/>(float, default=0.9)
            <br/><br/>
            If tol resulted in any group of annotations with more than 4 Annotations, then tol is multiplied by factor and the grouping is performed again
            <hr/>
            <b>min_tol</b><br/>(float, default=0.1)
            <br/><br/>
            If tol is reduced below min_tol (see the factor parameter), then the routine exits because we conclude that the annotation groups cannot be automatically reduced to have groups with each group having Annotations<=4
            <hr/>
            <b>return_distance_matrix</b><br/>(bool, default False)
            <br/><br/>
            Optionally return the distance matrix that was used to produce the clusters
            <hr/>
            <b>verbose </b><br/>(bool, default False)
            <br/><br/>
            If True, a warning message is printed when tol < min_tol occurs
        </div>
    </td>
    <td width="30%">
        <div align="center">
            Estimate which annotations refer to the same physical nodule in the CT scan. This method clusters all nodule Annotations for a Scan by computing a distance measure between the annotations [Returns a list of lists]
        </div>
    </td>
  </tr>

  <tr>
    <td width="5%">
        <div align="center">
        <b>get_path_to_dicom_files()</b>
        </div>
    </td>
    <td width="65%">
        <div align="center">
        None
        </div>
    </td>
    <td width="30%">
        <div align="center">
            Get the path to where the DICOM files are stored for this scan, relative to the root path set in the pylidc configuration file
        </div>
    </td>
  </tr>

  <tr>
    <td width="5%">
        <div align="center">
        <b>load_all_dicom_images()</b>
        </div>
    </td>
    <td width="65%">
        <div align="center">
            <b>verbose</b><br/>(bool)
            <br/><br/>
            Turn the loading method on/off
        </div>
    </td>
    <td width="30%">
        <div align="center">
            Get the path to where the DICOM files are stored for this scan, relative to the root path set in the pylidc configuration file
        </div>
    </td>
  </tr>

  <tr>
    <td width="5%">
        <div align="center">
        <b>to_volume()</b>
        </div>
    </td>
    <td width="65%">
        <div align="center">
            <b>verbose</b><br/>(bool)
            <br/><br/>
            Turn the loading method on/off
        </div>
    </td>
    <td width="30%">
        <div align="center">
            Return the scan as a 3D numpy array volume
        </div>
    </td>
  </tr>

  <tr>
    <td width="5%">
        <div align="center">
        <b>visualize()</b>
        </div>
    </td>
    <td width="65%">
        <div align="center">
            <b>annotation_groups</b><br/>(list of lists of Annotation objects, default=None)
            <br/><br/>
            This argument should be supplied by the returned object from the cluster_annotations method
        </div>
    </td>
    <td width="30%">
        <div align="center">
            Visualize the scan
        </div>
    </td>
  </tr>
</table>

### [Scan Class] Code Snippets

<div align="right">

> Usage example of the Scan class
</div>

```python
import pylidc as pl

scans = pl.query(pl.Scan).filter(pl.Scan.slice_thickness <= 1)
print(scans.count())
# => 97

scan = scans.first()
print(scan.patient_id,
      scan.pixel_spacing,
      scan.slice_thickness,
      scan.slice_spacing)
# => LIDC-IDRI-0066, 0.63671875, 0.6, 0.5

print(len(scan.annotations))
# => 11
```

<div align="right">

> cluster_annotations usage example
</div>

```python
import pylidc as pl

scan = pl.query(pl.Scan).first()
nodules = scan.cluster_annotations()

print("This can has %d nodules." % len(nodules))
# => This can has 4 nodules.

for i,nod in enumerate(nodules):
    print("Nodule %d has %d annotations." % (i+1,len(nod)))
# => Nodule 1 has 4 annotations.
# => Nodule 2 has 4 annotations.
# => Nodule 3 has 1 annotations.
# => Nodule 4 has 4 annotations.
```

<div align="right">

> load_all_dicom_images usage example
</div>

```python
import pylidc as pl
import matplotlib.pyplot as plt

scan = pl.query(pl.Scan).first()

images = scan.load_all_dicom_images()
zs = [float(img.ImagePositionPatient[2]) for img in images]
print(zs[1] - zs[0], img.SliceThickness, scan.slice_thickness)

plt.imshow( images[0].pixel_array, cmap=plt.cm.gray )
plt.show()
```
<div align="right">

> Visualize the scan
</div>

```python
import pylidc as pl

scan = pl.query(pl.Scan).first()
nodules = scan.cluster_annotations()

scan.visualize(annotation_groups=nodules)
```

## Annotation Class

> The Nodule model class holds the information from a single physicians annotation of a nodule >= 3mm class with a particular scan. A nodule has many contours, each of which refers to the contour drawn for nodule in each scan slice.

### [Annotation Class] Attributes

According to the Documentation an instance of [Annotation](https://pylidc.github.io/annotation.html) contains the following Attributes:

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
        <br/><br/>
        <b>Subtlety</b>
        </div>
    </td>
    <td width="5%">
        <div align="center">
            Integer
            <br/><br/>
            String
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
        <br/><br/>
        <b>InternalStructure</b>
        </div>
    </td>
    <td width="5%">
        <div align="center">
            Integer
            <br/><br/>
            String
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
        <br/><br/>
        <b>Calcification</b>
        </div>
    </td>
    <td width="5%">
        <div align="center">
            Integer
            <br/><br/>
            String
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
        <br/><br/>
        <b>Sphericity</b>
        </div>
    </td>
    <td width="5%">
        <div align="center">
            Integer
            <br/><br/>
            String
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
        <br/><br/>
        <b>Margin</b>
        </div>
    </td>
    <td width="5%">
        <div align="center">
            Integer
            <br/><br/>
            String
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
        <br/><br/>
        <b>Lobulation</b>
        </div>
    </td>
    <td width="5%">
        <div align="center">
            Integer
            <br/><br/>
            String
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
        <br/><br/>
        <b>Spiculation</b>
        </div>
    </td>
    <td width="5%">
        <div align="center">
            Integer
            <br/><br/>
            String
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
        <br/><br/>
        <b>Texture</b>
        </div>
    </td>
    <td width="5%">
        <div align="center">
            Integer
            <br/><br/>
            String
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
        <br/><br/>
        <b>Malignancy</b>
        </div>
    </td>
    <td width="5%">
        <div align="center">
            Integer
            <br/><br/>
            String
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
  
  <tr>
    <td width="5%">
        <div align="center">
        <b>centroid</b>
        </div>
    </td>
    <td width="5%">
        <div align="center">
            ndarray, shape=(3,)
        </div>
    </td>
    <td width="30%">
        <div align="center">-</div>
    </td>
    <td width="60%">
        <div align="center">
            The center of mass of the nodule as determined by its radiologist-drawn contours.
        </div>
    </td>
  </tr>

  <tr>
    <td width="5%">
        <div align="center">
        <b>contour_slice_indices</b>
        </div>
    </td>
    <td width="5%">
        <div align="center">
            ndarray
        </div>
    </td>
    <td width="30%">
        <div align="center">-</div>
    </td>
    <td width="60%">
        <div align="center">
            Array of indices from the scan where each contour belongs.
        </div>
    </td>
  </tr>

  <tr>
    <td width="5%">
        <div align="center">
        <b>contour_slice_zvals</b>
        </div>
    </td>
    <td width="5%">
        <div align="center">
            ndarray
        </div>
    </td>
    <td width="30%">
        <div align="center">-</div>
    </td>
    <td width="60%">
        <div align="center">
            Array of unique z-coordinates for the contours
        </div>
    </td>
  </tr>

  <tr>
    <td width="5%">
        <div align="center">
        <b>contours_matrix</b>
        </div>
    </td>
    <td width="5%">
        <div align="center">
            ndarray
        </div>
    </td>
    <td width="30%">
        <div align="center">-</div>
    </td>
    <td width="60%">
        <div align="center">
            All the contour index values inside a 3D numpy array
        </div>
    </td>
  </tr>

  <tr>
    <td width="5%">
        <div align="center">
        <b>diameter</b>
        </div>
    </td>
    <td width="5%">
        <div align="center">
            float
        </div>
    </td>
    <td width="30%">
        <div align="center">-</div>
    </td>
    <td width="60%">
        <div align="center">
            The maximal diameter as float, accounting for the axial-plane resolution of the scan. The units are mm
        </div>
    </td>
  </tr>

  <tr>
    <td width="5%">
        <div align="center">
        <b>surface_area</b>
        </div>
    </td>
    <td width="5%">
        <div align="center">
            float
        </div>
    </td>
    <td width="30%">
        <div align="center">-</div>
    </td>
    <td width="60%">
        <div align="center">
            Estimate the surface area by summing the areas of a trianglation of the nodules surface in 3d. The estimated surface area in squared millimeters.
        </div>
    </td>
  </tr>

  <tr>
    <td width="5%">
        <div align="center">
        <b>volume</b>
        </div>
    </td>
    <td width="5%">
        <div align="center">
            float
        </div>
    </td>
    <td width="30%">
        <div align="center">-</div>
    </td>
    <td width="60%">
        <div align="center">
            The estimated 3D volume of the annotated nodule. Units are cubic millimeters
        </div>
    </td>
  </tr>
</table>

### [Annotation Class] Methods

According to the Documentation an instance of [Annotation](https://pylidc.github.io/annotation.html) contains the following Methods:

<table width="100%" border="1" cellpadding="5">
  <tr>
    <th colspan="3" height="100%">
        <div align="center">
            Annotation Class Methods
        </div>
    </th>
  </tr>
  
  <tr>
    <td width="5%">
        <div align="center">
        <b>Method</b>
        </div>
    </td>
    <td width="65%">
        <div align="center">
        <b>Arguments</b>
        </div>
    </td>
    <td width="30%">
        <div align="center">
        <b>Returns</b>
        </div>
    </td>
  </tr>

  <tr>
    <td width="5%">
        <div align="center">
        <b>bbox()</b>
        </div>
    </td>
    <td width="65%">
        <div align="center">
            <b>pad</b><br/> (int, list of ints, or float, default=None)
            <br/><br/>
            Slice indices' bounding box with at least pad millimeters along each coordinate axis direction
        </div>
    </td>
    <td width="30%">
        <div align="center">
            Returns a tuple of Python slice objects that can be used to index into the image volume corresponding to the extent of the (padded) bounding box
        </div>
    </td>
  </tr>

  <tr>
    <td width="5%">
        <div align="center">
        <b>bbox_dims()</b>
        </div>
    </td>
    <td width="65%">
        <div align="center">
            <b>pad</b><br/> (int, list of ints, or float, default=None)
            <br/><br/>
            Slice indices' bounding box with at least pad millimeters along each coordinate axis direction
        </div>
    </td>
    <td width="30%">
        <div align="center">
            Return the physical dimensions of the nodule bounding box in millimeters along each coordinate axis [Eg: dims[i] is the length in millimeters of the bounding box along the coordinate axis i]
        </div>
    </td>
  </tr>

  <tr>
    <td width="5%">
        <div align="center">
        <b>bbox_matrix()</b>
        </div>
    </td>
    <td width="65%">
        <div align="center">
            <b>pad</b><br/> (int, list of ints, or float, default=None)
            <br/><br/>
            Slice indices' bounding box with at least pad millimeters along each coordinate axis direction
        </div>
    </td>
    <td width="30%">
        <div align="center">
            The bbox function returns a tuple of slices to be used to index into an image volume. On the other hand, bbox_array returns a 3x2 matrix where each row is the (start, stop) indices of the i, j, and k axes [Eg: bb_mat[i] is the stop and start indices (inclusive) of the bounding box along coordinate axis i]
        </div>
    </td>
  </tr>

  <tr>
    <td width="5%">
        <div align="center">
        <b>boolean_mask()</b>
        </div>
    </td>
    <td width="65%">
        <div align="center">
            <b>pad</b> <br/> (int, list of ints, or float, default=None)
            <br/><br/>
            Slice indices' bounding box with at least pad millimeters along each coordinate axis direction
            <hr/>
            <b>bbox</b> <br/> (3x2 NumPy array, default=None)
            <br/><br/>
            If bbox is provided, then pad is ignored. This argument allows for more fine-tuned control of placement of the mask in a volume
        </div>
    </td>
    <td width="30%">
        <div align="center">
            A boolean volume where 1 indicates nodule and 0 indicates non-nodule. The mask volume covers the extent of the voxels in the image volume given by annotation.bbox, i.e., the mask volume would be placed in the full image volume according to the bbox attribute
        </div>
    </td>
  </tr>

  <tr>
    <td width="5%">
        <div align="center">
        <b>feature_vals()</b>
        </div>
    </td>
    <td width="65%">
        <div align="center">
            <b>return_str</b> <br/> (bool, default=False)
            <br/><br/>
            If True, a list of strings is also returned, corresponding to the meaning of each numerical feature value.
        </div>
    </td>
    <td width="30%">
        <div align="center">
            Returns all feature values as a numpy array in the order presented in feature_names [It returns fvals[, fstrs]: fvals is an array of numerical values corresponding to the numerical feature values for the annotation. fstrs is a list of semantic string interpretations of the numerical values given in fvals]
        </div>
    </td>
  </tr>
  
  <tr>
    <td width="15%">
        <div align="center">
        <b>print_formatted_feature_table()</b>
        </div>
    </td>
    <td width="65%">
        <div align="center">
            None
        </div>
    </td>
    <td width="30%">
        <div align="center">
            Prints all feature values as a string table
        </div>
    </td>
  </tr>

  <tr>
    <td width="5%">
        <div align="center">
        <b>uniform_cubic_resample()</b>
        </div>
    </td>
    <td width="65%">
        <div align="center">    
            <b>side_length</b> <br/> (integer, default=None)
            <br/><br/>
            The physical length of each side of the new cubic volume in millimeters
            <hr/>
            <b>resample_vol</b> <br/> (boolean, default=True) 
            <br/><br/>
            If False, only the segmentation volume is resampled
            <hr/>
            <b>irp_pts</b> <br/> (3-tuple from meshgrid)
            <br/><br/>
            If provided, the volume(s) will be resampled over these interpolation points, rather than the automatically calculated points
            <hr/>
            <b>return_irp_pts</b> <br/> (boolean, default=False)
            <br/><br/>
            If True, the interpolation points (ix,iy,iz) at which the volume(s) were resampled are returned
            <hr/>
            <b>verbose</b> <br/> (boolean, default=True)
            <br/><br/>
            Turn the loading statement on / off
        </div>
    </td>
    <td width="30%">
        <div align="center">
            Get the CT value volume and respective boolean mask volume. The volumes are interpolated and resampled to have uniform spacing of 1mm along each dimension. The resulting volumes are cubic of the specified side_length. Thus, the returned volumes have dimensions, (side_length+1,)*3 (since side_length is the spacing) [[ct_volume,] mask [, irp_pts]]
        </div>
    </td>
  </tr>

  <tr>
    <td width="5%">
        <div align="center">
        <b>visualize_in_3d()</b>
        </div>
    </td>
    <td width="65%">
        <div align="center">
            <b>edgecolor</b> <br/> (string color or rgb 3-tuple)
            <br/><br/>
            Sets edgecolors of triangulation. Ignored if backend != matplotlib
            <hr/>
            <b>cmap</b> <br/> (matplotlib colormap string)
            <br/><br/>
            Sets the facecolors of the triangulation
            <hr/>
            <b>step</b> <br/> (int, default=1)
            <br/><br/>
            The step_size parameter for the skimage marching_cubes function
            <hr/>
            <b>figsize</b> <br/> (tuple, default=(5,5))
            <br/><br/>
            Figure size for the displayed volume
            <hr/>
            <b>backend</b> <br/> (string)
            <br/><br/>
            The backend for visualization. Default is matplotlib
        </div>
    </td>
    <td width="30%">
        <div align="center">
            Visualize in 3d a triangulation of the nodule’s surface
        </div>
    </td>
  </tr>

  <tr>
    <td width="5%">
        <div align="center">
        <b>visualize_in_scan()</b>
        </div>
    </td>
    <td width="65%">
        <div align="center">
            <b>verbose</b> <br/> (bool, default=True)
            <br/><br/>
            Turn the image loading statement on/off
        </div>
    </td>
    <td width="30%">
        <div align="center">
            Engage an interactive visualization of the slices of the scan along with scan and annotation information
        </div>
    </td>
  </tr>
 </table>

### [Annotation Class] Code Snippets

<div align="right">

> Short usage example for the Annotation class
</div>

```python
import pylidc as pl

# Get the first annotation with spiculation value greater than 3.
ann = pl.query(pl.Annotation)\
        .filter(pl.Annotation.spiculation > 3).first()

print(ann.spiculation)
# => 4

# Each nodule feature has a corresponding property
# to print the semantic value.
print(ann.Spiculation)
# => Medium-High Spiculation

ann = anns.first()
print("%.2f, %.2f, %.2f" % (ann.diameter,
                            ann.surface_area,
                            ann.volume))
# => 17.98, 1221.40, 1033.70
```


<div align="right">

> Illustration of the various pad argument types
</div>

```python
import pylidc as pl

ann = pl.query(pl.Annotation).first()
vol = ann.scan.to_volume()

print ann.bbox()
# => (slice(151, 185, None), slice(349, 376, None), slice(44, 50, None))

print(vol[ann.bbox()].shape)
# => (34, 27, 6)

print(vol[ann.bbox(pad=2)].shape)
# => (38, 31, 10)

print(vol[ann.bbox(pad=[(1,2), (3,0), (2,4)])].shape)
# => (37, 30, 12)

print(max(ann.bbox_dims()))
# => 21.45

print(vol[ann.bbox(pad=30.0)].shape)
# => (48, 49, 12)

print(ann.bbox_dims(pad=30.0))
# => [30.55, 31.200000000000003, 33.0]
```

<div align="right">

> Comparison between the bounding box volume vs the nodule volume
</div>

```python
import pylidc as pl

ann = pl.query(pl.Annotation).first()

print("%.2f mm^3, %.2f mm^3" % (ann.volume,
                                np.prod(ann.bbox_dims())))
# => 2439.30 mm^3, 5437.58 mm^3
```

<div align="right">

> Difference between bbox and bbox_matrix
</div>

```python
import pylidc as pl
ann = pl.query(pl.Annotation).first()

bb = ann.bbox()
bm = ann.bbox_matrix()

print(all([bm[i,0] == bb[i].start for i in range(3)]))
# => True

print(all([bm[i,1]+1 == bb[i].stop for i in range(3)]))
# => True
```

<div align="right">

> Usage of boolean_mask
</div>

```python
import pylidc as pl
import matplotlib.pyplot as plt

ann = pl.query(pl.Annotation).first()
vol = ann.scan.to_volume()

mask = ann.boolean_mask()
bbox = ann.bbox()

print("Avg HU inside nodule: %.1f" % vol[bbox][mask].mean())
# => Avg HU inside nodule: -280.0

print("Avg HU outside nodule: %.1f" % vol[bbox][~mask].mean())
# => Avg HU outside nodule: -732.2
```

<div align="right">

> Plot the centroid on a CT image slice
</div>

```python
import pylidc as pl
import matplotlib.pyplot as plt

ann = pl.query(pl.Annotation).first()
i,j,k = ann.centroid

vol = ann.scan.to_volume()

plt.imshow(vol[:,:,int(k)], cmap=plt.cm.gray)
plt.plot(j, i, '.r', label="Nodule centroid")
plt.legend()
plt.show()
```

<div align="right">

> Clarification example of the contour_slice_indices method
</div>

```python
import pylidc as pl

ann = pl.query(pl.Annotation)

zvals = ann.contour_slice_zvals
kvals = ann.contour_slice_indices
scan_zvals = ann.scan.slice_zvals

for k,z in zip(kvals, zvals):
    # the two z values should the same (up to machine precision)
    print(k, z, scan_zvals[k])
```

<div align="right">

> Usage example of the uniform_cubic_resample method
</div>

```python
import numpy as np
import matplotlib.pyplot as plt
import pylidc as pl

ann = pl.query(pl.Annotation).first()

# resampled volumes will have uniform side length of 70mm and
# uniform voxel spacing of 1mm.
n = 70
vol,mask = ann.uniform_cubic_resample(n)

# Setup the plot.
img = plt.imshow(np.zeros((n+1, n+1)),
                 vmin=vol.min(), vmax=vol.max(),
                 cmap=plt.cm.gray)


# View all the resampled image volume slices.
for i in range(n+1):
    img.set_data(vol[:,:,i] * (mask[:,:,i]*0.6+0.2))

    plt.title("%02d / %02d" % (i+1, n))
    plt.pause(0.1)
```

<div align="right">

> Visualize in 3d a triangulation of the nodule’s surface
</div>

```python
ann = pl.query(pl.Annotation).first()
ann.visualize_in_3d(edgecolor='green', cmap='autumn')
```

## Contour Class

> The Contour class holds the nodule boundary coordinate data of a pylidc.Annotation object for a single slice in the CT volume.

### [Contour Class] Attributes

According to the Documentation an instance of [Contour](https://pylidc.github.io/contour.html) contains the following Attributes:

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
        <b>Description and Return Values</b>
        </div>
    </td>
  </tr>

  <tr>
    <td width="15%">
        <div align="center">
        <b>to_matrix()</b>
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

