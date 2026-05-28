<template>
  <div class="bg-white border border-gray-200 rounded-2xl p-8 mb-10 card-shadow hover:card-shadow-hover transition-all duration-300">
    <!-- Card Header -->
    <div class="flex justify-between items-center mb-8 pb-6 border-b border-gray-200">
      <h2 class="text-3xl font-bold text-gray-900 uppercase tracking-wider">
        {{ report.month }}
      </h2>
      <div class="flex items-center gap-3">
        <span class="text-sm text-gray-500 uppercase tracking-wide">Total:</span>
        <span class="text-2xl font-bold text-gray-900">{{ report.totalHours }}h</span>
      </div>
    </div>

    <!-- Categories Summary Grid -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-10">
      <div
        v-for="category in report.categories"
        :key="category.name"
        class="bg-gray-50 border border-gray-200 rounded-xl p-6 hover:shadow-lg transition-all duration-300 hover:-translate-y-1"
      >
        <div class="flex justify-between items-center mb-2">
          <span class="text-base font-semibold text-gray-700 uppercase tracking-wide">
            {{ category.name }}
          </span>
          <span class="text-lg font-bold" :class="getCategoryTextColor(category.name)"> {{ category.percentage.toFixed(1) }}% </span>
        </div>
        <div class="text-4xl font-bold text-gray-900 mb-4"> {{ category.hours }}h </div>
        <div class="w-full h-2 bg-gray-200 rounded-full overflow-hidden">
          <div
            class="h-full rounded-full transition-all duration-1000"
            :style="{ width: category.percentage + '%' }"
            :class="getCategoryBgColor(category.name)"
          ></div>
        </div>
      </div>
    </div>

    <!-- Chart Section -->
    <div class="bg-gray-50 border border-gray-200 rounded-xl p-6 mb-10">
      <PieChart :data="chartData" :options="chartOptions" />
    </div>

    <!-- Detailed Entries -->
    <div class="bg-gray-50 border border-gray-200 rounded-xl p-8">
      <h3 class="text-xl font-bold text-gray-900 mb-6 uppercase tracking-wider"> Work Log Details </h3>
      <div v-for="category in report.categories" :key="category.name">
        <h4 v-if="category.entries.length > 0" class="text-base font-semibold uppercase tracking-wide mt-6 mb-4" :class="getCategoryTextColor(category.name)">
          {{ category.name }}
        </h4>
        <div class="grid gap-3">
          <div
            v-for="(entry, index) in category.entries"
            :key="index"
            class="bg-white border border-gray-200 rounded-lg p-4 hover:border-gray-400 hover:shadow-md transition-all duration-200 hover:translate-x-1"
          >
            <div class="text-gray-700 text-sm leading-relaxed mb-3">
              {{ entry["Work Description"] }}
            </div>
            <div class="flex gap-6 text-sm">
              <span class="font-semibold" :class="getCategoryTextColor(category.name)"> {{ entry["Billed Hours"] }}h </span>
              <span class="text-gray-500">
                {{ formatDate(entry["Work date"]) }}
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from "vue";
import PieChart from "./PieChart.vue";
import { useChartData } from "../composables/useChartData.js";

const props = defineProps({
  report: {
    type: Object,
    required: true,
  },
});

const reportRef = computed(() => props.report);
const { chartData, chartOptions } = useChartData(reportRef);

const getCategoryTextColor = (name) => {
  const colors = {
    Finca: "text-finca",
    Isabelgroup: "text-isabel",
    Freetime: "text-freetime",
  };
  return colors[name] || "text-gray-900";
};

const getCategoryBgColor = (name) => {
  const colors = {
    Finca: "bg-finca",
    Isabelgroup: "bg-isabel",
    Freetime: "bg-freetime",
  };
  return colors[name] || "bg-gray-400";
};

const formatDate = (dateStr) => {
  if (!dateStr) return "-";
  const date = new Date(dateStr);
  return date.toLocaleDateString("en-US", {
    month: "short",
    day: "numeric",
    year: "numeric",
  });
};
</script>
