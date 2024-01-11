# HFT Middleware Shopping List

## About The Project
The HFT Middleware Shopping List is a full-stack application designed to manage shopping lists efficiently. It provides an intuitive UI for users to add, edit, and delete items from their shopping list and a robust backend service built with modern technologies.

## Getting Started

### Prerequisites
- Node.js
- Python 3.11
- Docker

### Installation
1. Clone the repo:
```bash
git clone https://github.com/airbeat92/hft-middleware-shoppinglist.git
```
Navigate to the shoppinglist-ui and install NPM packages:

```bash
cd shoppinglist-ui
npm install
```
Navigate to the shoppinglist-service and install Python dependencies:
```bash
cd ../shoppinglist-service
poetry install
```
## Usage
### Start backend:

Navigate to the shoppinglist-service directory.
Install the dependencies with poetry: poetry install.
Start the backend server: poetry run python -m src.main

### Start the frontend:

Navigate to the shoppinglist-ui directory.
Install the NPM packages: npm install.
Start the development environment with Vite: npm run dev.

## Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.