### Style Guide for Expanding the Dataset of Historical Records

#### Purpose
This guide aims to standardize and facilitate the expansion of the dataset used for transcribing historical "ten-year tables" (tables décennales) from French and Belgian civil records. It ensures consistency, accuracy, and usability for future contributors.

---

### Data Structure
The dataset is a JSON file with each entry representing a single record containing:
- **`path`**: The file path of the corresponding image (e.g., `"table0.png"`).
- **`trans`**: The transcription of the record in the image.

#### Example Entry:
```json
{
  "path": "table0.png",
  "trans": "Barne huile 14 janvier 88"
}
```

---

### Data Formatting Guidelines

1. **File Path (`path`)**:
   - Use descriptive and sequential filenames (e.g., `table100.png`).
   - Ensure filenames are unique and correspond accurately to the image.

2. **Transcription (`trans`)**:
   - Transcribe text as it appears in the record, maintaining original spelling, capitalization, and punctuation.
   - For dates, replicate historical notation (e.g., "7bre" for September, "Xbre" for December).
   - Do not expand abbreviations or correct misspellings; preserve authenticity.

---

### Transcription Rules

#### Names:
- Preserve the order of names as written.
- Separate names with a single space (e.g., `"Jean Louis"`).

#### Dates:
- Transcribe exactly as written, even if non-standard.
- Abbreviations for months (e.g., "8bre" for October) should not be modernized.

#### Special Cases:
- **Illegible Text**: Use asterisks (`*`) to denote unclear portions (e.g., `"Jean *** 5 août 88"`).
- **Annotations**: Include additional notations in parentheses if visible and relevant (e.g., `"Décédé le 15 juillet 1851 (mortuary note)"`).

---

### Image Handling

1. Ensure all images are cropped to focus on the text.
2. Convert images to high-contrast black-and-white for clarity before transcription.
3. Maintain consistent resolution and quality.

---

### Dataset Expansion

#### Inclusion Criteria:
- Records must come from French or Belgian ten-year tables (1830–1924).
- Include as many regions and styles as possible to capture diversity.

#### Regional Variations:
- Note unique regional language or script differences.
- Prioritize entries that feature orthographic or stylistic diversity.

---

### Metadata and Context

1. **Region**: Maintain a mapping of image file paths to regions to enable filtering by locale.
2. **Record Type**: Specify if the record is a birth, marriage, or death.

---

### Validation and Quality Control

1. **Double-Check**: Cross-verify transcriptions against original images.
2. **Peer Review**: Have another contributor review new entries for accuracy.
3. **Consistency Checks**: Ensure uniformity in formatting and adherence to guidelines.

---

### Additional Tools and Practices

1. **OCR Assistance**:
   - Use the OCR model described in the paper to generate initial transcriptions, then manually verify and correct them.
   
2. **Data Augmentation**:
   - Include variations in handwriting, ink quality, and document condition to improve OCR robustness.

3. **Collaboration**:
   - Encourage contributors to document challenges or ambiguities in transcriptions for continuous improvement.

---

### Submission Process
1. Update the JSON file with new entries.
2. Provide a brief summary of changes, including:
   - Number of records added.
   - Regions or styles represented in the additions.

3. Submit new entries alongside original images for archival purposes.

---

### Future Enhancements
- Develop automated validation scripts to detect common errors.
- Encourage contributors to add metadata fields (e.g., `region`, `language`) for richer datasets.

This guide ensures uniformity and facilitates collaboration while preserving the historical integrity of the dataset.
