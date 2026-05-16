# CNAS rules

- To create a new page, refer to the pages/test folder and create a new directory under pages, then write the new script. 
- Next, generate an icon appropriate for its purpose in static/icons and register it on the pages/front page.
- Finally, ensure that a comment describing the page's purpose is added immediately below the class definition.

# Folder structure
```
root
├── cnas            cnas root folder
│   ├── componets   html rendering components
│   ├── pages       service pages for each features
│   │   ├── base    a common base page used across the application, such as an error page.
│   │   └── test    a test page used as a reference when creating a new page.
│   ├── route       url routing rules
│   ├── services    background service and running process
│   ├── static      web static resources
│   └── util        util scripts
├── test_assets     test resources
│   ├── documents
│   ├── images
│   ├── musics
│   └── videos
└── run.sh
```

# Rule files

| path | objective |
|------|-----------|
|docs/karpath-guidelines.md | Please follow this as a general guideline at all times. |
|docs/python-flask.md | You must read and follow these rules for Python coding. |
|docs/features.md | This is a description of the features that need to be implemented. |