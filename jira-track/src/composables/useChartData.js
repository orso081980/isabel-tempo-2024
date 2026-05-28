/**
 * useChartData Composable
 * Manages chart data preparation and configuration
 * Separates chart logic from presentation
 */
import { computed } from "vue";
import { ChartConfigService } from "../services/ChartConfigService.js";

export function useChartData(report) {
  const chartData = computed(() => {
    if (!report.value) return null;

    const { labels, values } = report.value.getChartData();
    return ChartConfigService.getPieChartData(labels, values);
  });

  const chartOptions = computed(() => {
    return ChartConfigService.getPieChartOptions();
  });

  return {
    chartData,
    chartOptions,
  };
}
