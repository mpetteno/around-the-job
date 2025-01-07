<template>
  <div id="map">
    <Filters />
  </div>
</template>

<script setup>
  import { onMounted, watch } from "vue";
  import "leaflet/dist/leaflet.css";
  import L from "leaflet";
  import { bivouacs } from '@/store.js'
  import Filters from "@/components/bivouacs/Filters.vue";

  // Parameters
  const props = {
    mapUrl: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
    mapCenter: [46.14192843759422, 12.215843388699499],
    mapInitialZoom: 8,
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

  function bivouacPopup(bivouac) {
    let popupHtml = `<div class="popup-container">`;
    // Name
    if (bivouac.name) popupHtml += `<h4>${bivouac.name}</h4>`;
    // Preview Image
    if (bivouac.preview_image_link) {
      popupHtml += `<div class="image-container"><img src="${bivouac.preview_image_link}" alt="Preview Image" class="popup-image" /></div>`;
    }
    // Altitude
    if (bivouac.altitude) popupHtml += `<p><span class="label">Altitude:</span> ${bivouac.altitude} meters</p>`;
    // Walk Time
    if (bivouac.walk_time) popupHtml += `<p><span class="label">Walk Time:</span> ${bivouac.walk_time}</p>`;
    // Uphill
    if (bivouac.uphill) popupHtml += `<p><span class="label">Uphill:</span> ${bivouac.uphill} meters</p>`;
    // Difficulty
    if (bivouac.difficulty) popupHtml += `<p><span class="label">Difficulty:</span> ${bivouac.difficulty}</p>`;
    // Links Section: Website, GPX Track, and Parking Location
    const links = [];
    if (bivouac.website_link) {
      links.push(`<a href="${bivouac.website_link}" target="_blank">Website</a>`);
    }
    if (bivouac.gpx_track_link) {
      links.push(`<a href="${bivouac.gpx_track_link}" target="_blank">GPX</a>`);
    }
    if (bivouac.parking_location) {
      links.push(`<a href="${bivouac.parking_location}" target="_blank">Parking</a>`);
    }
    if (links.length > 0) {
      popupHtml += `<p><span class="label">Links:</span> ${links.join(', ')}</p>`;
    }
    // Facilities (Water, Wood, Kitchen, Fireplace, Stove)
    popupHtml += `<div class="facilities">`;
    popupHtml += `<p><span class="label">Water</span> ${bivouac.water ? '<span class="checkmark">✔</span>' : '<span class="cross">✘</span>'}</p>`;
    popupHtml += `<p><span class="label">Wood</span> ${bivouac.wood ? '<span class="checkmark">✔</span>' : '<span class="cross">✘</span>'}</p>`;
    popupHtml += `<p><span class="label">Kitchen</span> ${bivouac.kitchen ? '<span class="checkmark">✔</span>' : '<span class="cross">✘</span>'}</p>`;
    popupHtml += `<p><span class="label">Fireplace</span> ${bivouac.fireplace ? '<span class="checkmark">✔</span>' : '<span class="cross">✘</span>'}</p>`;
    popupHtml += `<p><span class="label">Stove</span> ${bivouac.stove ? '<span class="checkmark">✔</span>' : '<span class="cross">✘</span>'}</p>`;
    popupHtml += `</div>`;
    // Beds
    if (bivouac.beds) popupHtml += `<p><span class="label">Beds:</span> ${bivouac.beds}</p>`;
    // Notes
    if (bivouac.notes) popupHtml += `<p><span class="label">Notes:</span> ${bivouac.notes}</p>`;
    // Alternative Paths
    if (bivouac.alternative_paths) popupHtml += `<p><span class="label">Alternative Paths:</span> ${bivouac.alternative_paths}</p>`;
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
    bivouacs.value.forEach((bivouac) => {
      const markerOptions = bivouac.favourite ? {icon: favouriteIcon} : {icon: defaultIcon};
      const marker = L.marker([bivouac.latitude, bivouac.longitude], markerOptions)
        .addTo(map)
        .bindPopup(bivouacPopup(bivouac));
      markers.push(marker);
    });
  }
  watch(bivouacs, () => { updateMarkers(); });
</script>

<style>
.leaflet-popup-content p {
  margin: 7px;
}

.facilities {
  display: flex;
}

.facilities p {
  display: flex;
  flex-direction: column;
  align-items: center;
}


.image-container {
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
  margin-bottom: 10px;
}

.image-container img {
  width: 300px; /* Fixed width */
  height: 200px; /* Fixed height */
  object-fit: cover; /* Ensures the image covers the container without stretching */
  border-radius: 10px;
}

.checkmark {
  color: green;
  font-size: 18px;
}

.cross {
  color: red;
  font-size: 18px;
}
</style>
