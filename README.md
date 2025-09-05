# File Upload API

A simple and fast file upload web application built with FastAPI. This project provides a web interface for uploading files over a network with real-time progress tracking.

**Note:** The web interface is in Polish language.

## Features

- 📊 Real-time upload progress tracking
- 🚀 Fast asynchronous file handling
- 🌐 Network-accessible for easy file sharing
- 📱 Responsive web interface
- ⚡ Built with FastAPI for high performance

## Requirements

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) package manager

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd file_api
```

2. Install dependencies using uv:

```bash
uv sync
```

## Usage

### Quick Start

Run the application using the provided script:

```bash
chmod +x start.sh
./start.sh
```

Or run directly with uv:

```bash
uv run main.py
```

The application will:

- Start the server on `http://*:8000`
- Display your local IP addresses for network access
- Create an `uploads/` directory for storing uploaded files

### Accessing the Application

1. **Locally**: Open `http://localhost:8000` in your browser
2. **Network**: Use the IP address shown in the console (e.g., `http://192.168.1.100:8000`)

### Web Interface (Polish)

- **"Wybierz plik"**: Select file button
- **"Prześlij"**: Upload button
- **Progress bar**: Shows upload progress in real-time
- **File size display**: Shows current/total MB uploaded
- **Status messages**:
  - "Wysyłanie...": Uploading...
  - "Wysłano, przetwarzanie...": Sent, processing...
  - "Coś się zjebało :/"): Something went wrong :/
