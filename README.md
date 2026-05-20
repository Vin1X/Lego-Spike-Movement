# Lego-Spike-Movement
Lego-Spike-Prime using a Raspberry Pi Buildhat and Python

## Useful commands
Transfer sourcecode to Raspberry:
```scp -r src/ username@address:Path/to/destination```

Executing code:
```python Lego-Spike-Movement/src/main.py```

Transfer public ssh-key from your machine (No hassle with logging into pi because password is no longer needed)
```type C:\Users\Vince\.ssh\id_ed25519.pub | ssh pi@192.168.178.143 "cat >> .ssh/authorized_keys"```