# Personal Page Creator
Python script to create customizable website intended for GitHub pages.

Inspired by [Git Folio](https://github.com/imfunniee/gitfolio)

## Installing
To install the package, run - 
```bash
pip install personal-page-creator
```

Or view it at [PyPI](https://pypi.org/project/personal-page-creator/)

## Usage

### Initialize

Use init to initialize the config file
```bash
ppc init
```
Init will create a config file which is used to customize the page.

### Build

```bash
ppc build
```
Build will use the config file to generate the required HTML and CSS files.

### Serve

Want to check the output before hosting? Use 'serve' to start a local http server.

```bash
ppc serve
```

## Customizations

| Config Keys        | Input           | Functions     |
| -------------  |:-------------:|:---------------------|
| excluded | Specify a list of repo names | The specified repos will not be included as part of the site|
| side_background| URL | Image from the url will be used as side background of the site |
| social | Dict will key and value | Used to give links to the user's profile,Currenty supports linkedin, bitbucket and twitter |
| cv_path | URL or filename | Used to give download link to the user's cv ( Curriculum Vitae ) |

## Example 
Below is an example config file which uses are the available functions.

```json
{
    "username": "your-github-username",
    "excluded": [ "this-repo-will-be-excluded" ],
    "social" : {
        "linkedin": "linkedin_username",
        "twitter": "twitter_handle",
        "bitbucket": "bitbucket_username"
    },
    "side_background": "http://www.example.com/path/to/image.jpg",
    "cv_path": "path/to/cv.pdf"
}
```

## TODO

- Config to add organization repo also
- Add themes


