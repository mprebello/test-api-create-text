
# Django API Project

This project is a simple Django-based API that receives a GET request and appends the content to a text file.

## Requirements

- Python 3.x
- Django
- PyYAML

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/mprebello/test-api-create-text
   cd test-api-create-text
   
   #example to build the container
   docker build -t test .

   #example to run the container
   docker run -p 8000:8000 -ti test


# test-api-create-text
curl -k http://127.0.0.1:8000/create/add-text/?text=yourtexthere
