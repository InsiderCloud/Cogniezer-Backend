# Cogniezer-Backend

![GitHub license](https://img.shields.io/github/license/InsiderCloud/Cogniezer-Backend)
![GitHub repo size](https://img.shields.io/github/repo-size/InsiderCloud/Cogniezer-Backend)
![GitHub issues](https://img.shields.io/github/issues/InsiderCloud/Cogniezer-Backend)
![GitHub pull requests](https://img.shields.io/github/issues-pr/InsiderCloud/Cogniezer-Backend)
![GitHub last commit](https://img.shields.io/github/last-commit/InsiderCloud/Cogniezer-Backend)

## Overview

Cogniezer-Backend is the backbone of the Cogniezer project, aimed at providing real-time audio summarization services. Developed as part of the BSc Hons Computer Science program at the University of Kelaniya, this REST API leverages the power of FastAPI, Azure Speech-to-Text, and the T5-base transformer model. Our system is trained on a diverse range of datasets, ensuring robust and accurate summarization.

## Table of Contents

* [Features](#features)
* [Installation](#installation)
* [Docker Support](#docker-support)
* [API Endpoints](#api-endpoints)
* [Contributing](#contributing)
* [License](#license)
* [Acknowledgements](#acknowledgements)

## Features

* Audio to text summarization
* Integration with Azure Speech-to-Text
* Built using FastAPI for high performance
* Utilizes T5-base transformer model for summarization
* Trained on diverse datasets for robust performance

## Installation

### Prerequisites

* Python 3.7 or higher
* Conda
* Git

### Clone the Repository

```bash
git clone https://github.com/InsiderCloud/Cogniezer-Backend
```

### Setup the Environment

```bash
conda create -n cogniezer python=3.7
conda activate cogniezer
pip install -r requirements.txt
```

### Configure the Project

Update the configuration files with your settings:

```bash
.
├── config
│ ├── config.yaml
├── params.yaml
. 
```

### Environment Variables

Add the following environment variables to the `.env` file:

```txt
AZURE_KEY=your_azure_key
AZURE_REGION=your_azure_region
HOST=localhost
PORT=8000
```

### Run the Project

```bash
gunicorn app:app
```

## Docker Support

### Build the Docker Image

Modify the `IMAGE_NAME` and `IMAGE_TAG` in the `build.sh` file and run:

```
./build.sh
```

## API Endpoints

### Index

**GET** `/`

Returns the main page.

```
http://{host}:{port}/
```

### Text Summarization

**POST** `/api/predict`

Predicts the summary of the provided text.

```bash
curl -X POST http://{host}:{port}/api/predict \
    -H 'Content-Type: application/json' \
    -d '{"text": "Text to be summarized"}'
```

### Upload File

**POST** `/api/uploadfile/`

Uploads an audio file, transcribes it, and returns the summary.

```bash
curl -X POST http://{host}:{port}/api/uploadfile/ \
    -H 'Content-Type: multipart/form-data' \
    -F 'wav_file=@path_to_your_audio_file.wav'
```

## Contributing

We welcome contributions from the community! Please follow these steps to contribute:

* Fork the repository
* Create a new branch for your feature or bugfix
* Commit your changes
* Push the branch to your fork
* Open a pull request

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/InsiderCloud/Cogniezer-Backend/blob/main/LICENSE) file for details.

## Acknowledgements

* [FastAPI](https://fastapi.tiangolo.com/)
* [HuggingFace](https://huggingface.co/)
* [Azure Speech-to-Text](https://azure.microsoft.com/en-us/services/cognitive-services/speech-to-text/)
* [University of Kelaniya](https://www.kln.ac.lk/)
