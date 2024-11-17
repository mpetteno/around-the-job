# around-the-job
Repository for the Around the Job application

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).

## Customize configuration

See [Vite Configuration Reference](https://vite.dev/config/).

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```

### Lint with [ESLint](https://eslint.org/)

```sh
npm run lint
```

# Setup
1) Create Firebase project
2) Create Firebase app
3) Save config to json
4) ~~Check and ensure free tier limit on GCC~~ (firebase does not require a billing account)
5) Enable Google Maps Geocoding API for the project
6) Create API credentials
7) Create .env file with GOOGLE_API_KEY=
8) Download excel file without coordinates 
9) Run geocoding.py
10) Upload modified excel file to Drive and export CSV
11) Run upload_to_firebase.py