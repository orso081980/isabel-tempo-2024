<template>
  <div class="min-h-screen bg-white py-5 px-4">
    <!-- Header -->
    <header class="text-center py-10 mb-10 relative">
      <div class="absolute bottom-0 left-1/2 -translate-x-1/2 w-24 h-0.5 bg-gradient-to-r from-transparent via-gray-300 to-transparent"></div>
      <div class="max-w-3xl mx-auto">
        <h1 class="text-5xl font-bold text-gray-900 mb-4 tracking-wide flex items-center justify-center gap-4">
          <span class="text-4xl animate-pulse">⚡</span>
          Tempo Time Tracker
        </h1>
        <p class="text-lg text-gray-600 tracking-widest uppercase font-light"> Professional Time Management Dashboard </p>
      </div>
    </header>

    <!-- Main Content -->
    <main class="max-w-7xl mx-auto">
      <!-- Loading State -->
      <div v-if="loading" class="text-center py-24 text-gray-600">
        <div class="w-16 h-16 border-4 border-gray-200 border-t-gray-600 rounded-full mx-auto mb-6 animate-spin"></div>
        <p class="text-lg font-medium tracking-wide">Loading reports...</p>
      </div>

      <!-- Error State -->
      <div v-else-if="error" class="text-center py-24 bg-red-50 border border-red-200 rounded-2xl max-w-2xl mx-auto p-10">
        <div class="text-6xl mb-6">⚠️</div>
        <h3 class="text-red-600 text-2xl font-bold mb-4">Error Loading Reports</h3>
        <p class="text-gray-700 mb-8">{{ error }}</p>
        <button
          @click="loadReports"
          class="bg-red-500 hover:bg-red-600 text-white font-semibold px-8 py-3 rounded-lg uppercase tracking-wide transition-all duration-300 hover:-translate-y-0.5 hover:shadow-lg"
        >
          Retry
        </button>
      </div>

      <!-- Reports -->
      <div v-else class="grid gap-10">
        <TimeReportCard v-for="report in reports" :key="report.month" :report="report" />
      </div>
    </main>

    <!-- Footer -->
    <footer class="text-center py-10 mt-16 text-gray-500 text-sm border-t border-gray-200">
      <p>Powered by Vue.js 3 | Built with ❤️ for professional time tracking</p>
    </footer>
  </div>
</template>

<script setup>
import TimeReportCard from "./TimeReportCard.vue";
import { useTimeReports } from "../composables/useTimeReports.js";

const { reports, loading, error, loadReports } = useTimeReports();
</script>
