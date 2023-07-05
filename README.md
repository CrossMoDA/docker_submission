# crossMoDA Challenge - MICCAI 2023
Example docker container for the crossMoDA Challenge organized as part of MICCAI 2023. The script simply thresholds hrT2 images to "predict" the intra-/extra-meatal VS and cochlea.

## Build the Docker image
`Dockerfile` contains all the information used to create the Docker container. 
Speficically, it uses the `continuumio/miniconda` image and installs additionnal Python libraries. Then, it automatically executes a dummy algorithm `src/run_inference.py` on all the scans located in `/input/` and write the results in `/output/`.

To build the docker image:

```
docker build -f Dockerfile -t [your image]
```

## Docker commands
Containers submitted to the challenge will be run with the following commands:
```
docker run --rm -v [input directory]:/input/:ro -v [output directory]:/output -it [your image]
```
## Credits
This repository is based on the intructions provided for the MICCAI WMH segmentation challenge 2017. 
