# PROPSER hp

## Set up a virtual environment
To avoid the package dependency problems, we will use virtual environment by running the following command in the terminal.
```
python3 -m venv .venv
```


Then we need to activate the virtual environment which varies depending on your OS.
```
source .venv/bin/activate # Mac
```
```
.venv\Scripts\Activate.ps1 # Windows
```


Please confirm that you have the `(.venv)` in the terminal after activation. Then, update the pip and install the requirement packages in the requirements.txt file.    
```
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Now you are ready to go! Just run 
```
streamlit run main.py
```
The stremalit app will be launched in your browser. If you would like to stop the app, just press `Ctrl + C` in the terminal.

## Test local Docker image
Now we test the docker image locally. We will
```
docker build -t propser_test .
docker run -p 8081:8080 propser_test
```


## Deploy to Google Cloud Run
Once confirming that the docker image works, we will deploy the app to the google cloud platform.
First, we need to build the docker image and push it to the google cloud container registry. Then, we will deploy the app to the google cloud run.
```
gcloud builds submit --tag gcr.io/prosper1/prosper_hp:v0
```

```
gcloud run deploy prosper-hp \
  --image gcr.io/prosper1/prosper_hp:v0 \
  --platform managed \
  --region asia-northeast1 \
  --allow-unauthenticated --quiet
```



Gratitude to [this youtube playlist](https://www.youtube.com/playlist?list=PLvRfcAN-QbYnxloydunJlfES_m6GblyEt) for the inspiration.


