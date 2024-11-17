<template>
  <div id="map"></div>
  <ul>
    <li v-for="company in companies" v-if="companies">
      {{ company.company_name }}
    </li>
  </ul>
</template>

<script setup>
  import { onMounted } from "vue";
  import "leaflet/dist/leaflet.css";
  import L from "leaflet";
  import { collection } from "firebase/firestore";
  import { useFirestore, useCollection } from "vuefire";

  let map;
  const db = useFirestore();
  const companies = useCollection(collection(db, 'companies'))

  onMounted(() => {
    map = L.map("map").setView([51.505, -0.09], 13);
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      maxZoom: 19,
      attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    }).addTo(map);
  });
</script>

<style>
  #map {
    width: 100%;
    height: 100vh;
  }
</style>
