<template>
  <div id="map">
    <Filters />
    <Menu />
  </div>
</template>

<script setup>
  import { onMounted, watch } from "vue";
  import "leaflet/dist/leaflet.css";
  import L from "leaflet";
  import { companies } from '@/store.js'
  import Menu from "@/components/companies/Menu.vue";
  import Filters from "@/components/companies/Filters.vue";

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

  function companyPopup(company) {
    let popupHtml = `<div class="popup-container">`;
    if (company.name) popupHtml += `<h4>${company.name}</h4>`;
    if (company.description) popupHtml += `<p class="description">${company.description}</p>`;
    if (company.website_url) {
      popupHtml += `<p><span class="label">Website:</span> <a href="${company.website_url}" target="_blank">${company.website_url}</a></p>`;
    }
    if (company.carrers_page_url) {
      popupHtml += `<p><span class="label">Careers:</span> <a href="${company.carrers_page_url}" target="_blank">Careers Page</a></p>`;
    }
    if (company.contact_email) {
      popupHtml += `<p><span class="label">Email:</span> <a href="mailto:${company.contact_email}">${company.contact_email}</a></p>`;
    }
    if (company.phone) {
      popupHtml += `<p><span class="label">Phone:</span> +${company.phone}</p>`;
    }
    if (company.size) {
      popupHtml += `<p><span class="label">Company Size:</span> ${company.size}</p>`;
    }
    if (company.rating) {
      popupHtml += `<p><span class="label">Rating:</span> <span class="rating">${'★'.repeat(Math.floor(company.rating))} ${company.rating}</span></p>`;
    }
    popupHtml += `</div>`;
    return popupHtml;
  }

  // Setup markers
  const defaultIcon = L.divIcon({
    html: '<i class="fa-solid fa-location-dot"></i>',
    className: 'default-marker-icon',
  });
  const favouriteIcon = L.divIcon({
    html: '<i class="fa-solid fa-heart"></i>',
    className: 'favourite-marker-icon',
  });
  let markers = [];
  const updateMarkers = () => {
    // Remove all existing markers
    markers.forEach((marker) => map.removeLayer(marker));
    markers = [];
    // Add filtered companies as markers
    companies.value.forEach((company) => {
      const markerOptions = company.favourite ? {icon: favouriteIcon} : {icon: defaultIcon};
      const marker = L.marker([company.latitude, company.longitude], markerOptions)
        .addTo(map)
        .bindPopup(companyPopup(company));
      markers.push(marker);
    });
  }
  watch(companies, () => { updateMarkers(); });
</script>
