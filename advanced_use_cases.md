# Advanced Use Cases and Automation

For 

* [Setting Up A Workspace](#Setting)
* [Updating Template Fields in a PowerPoint File](#Updating)

----------

# Setting Up A Workspace

1. Set up and activate a virtual environment

```bash
python3 - m venv venv
. venv/bin/activate
```

2. Install `presalytics`

```bash
pip install presalytics
```

3. Set Configuration

```bash
presaltyics config {YOUR_USERNAME} # The primary email address on your account
```

4. Load story into workspace

```bash
presaltyics pull --id {STORY_ID} # The 36 digit fingerprint for the story 
```

----------

# Updating Template Fields in a PowerPoint File


