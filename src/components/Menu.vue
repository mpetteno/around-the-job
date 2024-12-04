<template>
  <Sidebar position="top">
    <nav>
      <div class="section">
        <div class="section-title">Boards</div>
        <a href="https://linkedin.com" target="_blank"><i class="fab fa-linkedin"></i>LinkedIn</a>
        <a href="https://www.indeed.com/worldwide" target="_blank"><i class="fas fa-globe"></i>Indeed</a>
        <a href="https://glassdoor.com" target="_blank"><i class="fas fa-door-open"></i>Glassdoor</a>
        <a href="https://ziprecruiter.com" target="_blank"><i class="fas fa-map-pin"></i>ZipRecruiter</a>
        <a href="https://careerbuilder.com" target="_blank"><i class="fas fa-briefcase"></i>CareerBuilder</a>
        <a href="https://monster.com" target="_blank"><i class="fas fa-paw"></i>Monster</a>
        <a href="https://www.workatastartup.com/" target="_blank"><i class="fa-solid fa-play"></i>Y Combinator</a>
        <a href="https://jobs.workable.com/" target="_blank"><i class="fas fa-clipboard-list"></i>Workable Jobs</a>
        <a href="https://soundlister.com" target="_blank"><i class="fas fa-music"></i>Soundlister</a>
        <a href="https://soundbetter.com" target="_blank"><i class="fas fa-guitar"></i>SoundBetter</a>
      </div>
      <div class="section">
        <div class="section-title">Tools</div>
        <a href="https://interviewprep.org/" target="_blank"><i class="fas fa-brain"></i>InterviewPrep</a>
        <a href="https://neetcode.io" target="_blank"><i class="fas fa-code"></i>NeetCode</a>
        <a href="https://leetcode.com/" target="_blank"><i class="fas fa-terminal"></i>LeetCode</a>
        <a href="https://hackerrank.com" target="_blank"><i class="fa-brands fa-hackerrank"></i>HackerRank</a>
      </div>
    </nav>
  </Sidebar>
</template>

<script setup>
  import Sidebar from "@/ui/Sidebar.vue";
</script>

<style scoped>
  .sidebar-container {
    width: 100%;
    flex-direction: column;
  }

  .sidebar-container >>> .sidebar {
    border-radius: 0 0 12px 12px;
  }

  .sidebar-container >>> .toggle-button {
    width: 56px;
    height: 24px;
    border-radius: 0 0 12px 12px;
    border-width: 0 1px 1px 1px;
  }

  nav {
    color: #363536;
    padding: 1em;
    font-size: 20px;
    display: flex;
    flex-direction: row;
    column-gap: 50px;
  }

  nav a {
    display: block;
    text-decoration: none;
    color: #363536;
    padding: 0.5em 0;
  }

  nav a:hover {
    color: #3899a2;
  }

  nav i {
    margin-right: 0.5em;
  }

  .section-title {
    color: #358692;
    font-weight: bold;
    margin-bottom: 0.5em;
  }
</style>
