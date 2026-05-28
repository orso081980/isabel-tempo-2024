/**
 * Chart Configuration Service
 * Handles all chart-related configuration and options
 * Follows Single Responsibility Principle
 */

export class ChartConfigService {
  static getColors() {
    return {
      isabelgroup: {
        background: "#1B2B4C",
        border: "#1B2B4C",
      },
      finca: {
        background: "rgba(239, 68, 68, 0.8)",
        border: "rgba(239, 68, 68, 1)",
      },
      freetime: {
        background: "rgba(6, 182, 212, 0.8)",
        border: "rgba(6, 182, 212, 1)",
      },
    };
  }

  static getCategoryColor(categoryName) {
    const colors = this.getColors();
    const key = categoryName.toLowerCase();
    return colors[key] || colors.finca;
  }

  static getChartColors(labels) {
    return labels.map((label) => this.getCategoryColor(label));
  }

  static getPieChartOptions() {
    return {
      responsive: true,
      maintainAspectRatio: true,
      plugins: {
        legend: {
          position: "bottom",
          labels: {
            color: "#374151",
            font: {
              family: "Inter",
              size: 14,
              weight: "600",
            },
            padding: 20,
            usePointStyle: true,
            pointStyle: "circle",
          },
        },
        tooltip: {
          backgroundColor: "rgba(255, 255, 255, 0.95)",
          titleColor: "#111827",
          bodyColor: "#374151",
          borderColor: "#E5E7EB",
          borderWidth: 1,
          padding: 16,
          cornerRadius: 8,
          displayColors: true,
          callbacks: {
            label: function (context) {
              return `${context.label}: ${context.parsed.toFixed(1)}%`;
            },
          },
        },
      },
    };
  }

  static getPieChartData(labels, values) {
    const colors = this.getChartColors(labels);

    return {
      labels,
      datasets: [
        {
          data: values,
          backgroundColor: colors.map((c) => c.background),
          borderColor: colors.map((c) => c.border),
          borderWidth: 2,
          hoverOffset: 15,
        },
      ],
    };
  }
}
