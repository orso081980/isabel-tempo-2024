/**
 * useTimeReports Composable
 * Manages time report state and loading logic
 * Follows Composition API best practices
 */
import { ref, onMounted } from "vue";
import { createDataService } from "../services/DataService.js";

export function useTimeReports() {
  const reports = ref([]);
  const loading = ref(true);
  const error = ref(null);
  const dataService = createDataService();

  const loadReports = async () => {
    loading.value = true;
    error.value = null;

    try {
      reports.value = await dataService.fetchReports();
    } catch (err) {
      error.value = err.message;
      console.error("Failed to load reports:", err);
    } finally {
      loading.value = false;
    }
  };

  onMounted(() => {
    loadReports();
  });

  return {
    reports,
    loading,
    error,
    loadReports,
  };
}
