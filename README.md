# Nomad: Aggregator API for locations

Nomad is a V1 aggregator API for locations, supporting Geocoding, weather, and radio list queries.



## Cloning the repository

Use [Git ](https://git-scm.com)to clone the repository with the following commands

```bash
git clone https://github.com/rvams/nomad.git
```

## Setting up a virtual environment

MacOS/ Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```
Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

## Installing and running locally

Make sure you are inside the folder and do this after creating a venv

```bash
#Install the dependencies
pip install -r requirements.txt

#Run the development server
fastapi dev main.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change. 

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)