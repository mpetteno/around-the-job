<template>
  <div id="map"></div>
</template>

<script setup>
  import { onMounted, watch } from "vue";
  import "leaflet/dist/leaflet.css";
  import '@fortawesome/fontawesome-free/css/all.min.css';
  import L from "leaflet";
  import { companies } from "@/store.js";

  // Parameters
  const props = {
    mapUrl: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
    mapCenter: [0, 0],
    mapInitialZoom: 2,
    mapMaxZoom: 19,
    attribution: ""
  }

  // Setup map
  let map;
  onMounted(() => {
    map = L.map("map").setView(props.mapCenter, props.mapInitialZoom);
    L.tileLayer(props.mapUrl, {
      maxZoom: props.mapMaxZoom,
      attribution: props.attribution
    }).addTo(map);
  });

  // Setup markers
  const favouriteIcon = L.divIcon({
    html: '<i class="fa-solid fa-heart"></i>',
    className: 'favourite-icon',
  });
  let markers = [];
  const updateMarkers = () => {
    // Remove all existing markers
    markers.forEach((marker) => map.removeLayer(marker));
    markers = [];
    // Add filtered companies as markers
    companies.value.forEach((company) => {
      const markerOptions = company.favourite ? {icon: favouriteIcon} : {};
      const marker = L.marker([company.latitude, company.longitude], markerOptions)
        .addTo(map)
        .bindPopup(`<b>${company.company_name}</b>`);
      markers.push(marker);
    });
  }
  watch(companies, () => { updateMarkers(); });
</script>

<style>
  #map {
    width: 100%;
    height: 100vh;
    overflow: hidden;
  }

  .favourite-icon {
    color: indianred;
    font-size: 32px;
  }
</style>
