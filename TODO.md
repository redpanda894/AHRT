### To Do List
- [ ] Modify Data set
    - [X] Convert all images from .tif and .png to .jpg
    - [X] Change all of the image references from .tif and .png to .jpg
    - [X] Prepend Generic/Belleville names to the imagefile names and also all references to the images
    - [ ] Make new .json
        - [ ] Make a union of all json char_sets
        - [ ] Add new train to json with all images from other jsons
        - [ ] Add new test to json with all images from other jsons
        - [ ] Add new valid to json with all images from other jsons
    - [ ] Make new images dir
        - [ ] Move all other train images to train a new dir
        - [ ] Move all other test images to train a new dir
        - [ ] Move all other valid images to train a new dir
    - [ ] Name new modified dataset
- [ ] Obtain data in the model
- [ ] Use default model format to create model
- [ ] Train model on handwritten names
- [ ] Make line segmentation specific to tables decennales
    - [ ] Make a dataset of segmented lines for tables (Several Books)
    - [ ] Split into validation and training (& transfer) sets
    - [ ] Train to identify borders
- [ ] Apply transfer learning with handwritten census records
- [ ] Analyze success on contemporary tables & review
