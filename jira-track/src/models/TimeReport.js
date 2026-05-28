/**
 * TimeReport Model
 * Represents a monthly time report with categories
 * Follows Single Responsibility Principle
 */
export class TimeReport {
  constructor(month, data) {
    this.month = month;
    this.categories = this.parseCategories(data);
    this.totalHours = this.calculateTotalHours();
  }

  parseCategories(data) {
    const categories = [];
    const categoryNames = ["finca", "isabelgroup", "freetime"];

    categoryNames.forEach((name) => {
      const timeKey = `${name}_time`;
      const percentageKey = `${name}_percentage`;
      const dataKey = `${name}_data`;

      if (data[timeKey] !== undefined) {
        categories.push({
          name: this.capitalize(name),
          hours: data[timeKey],
          percentage: data[percentageKey],
          entries: data[dataKey] || [],
        });
      }
    });

    return categories;
  }

  calculateTotalHours() {
    return this.categories.reduce((sum, cat) => sum + cat.hours, 0);
  }

  capitalize(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
  }

  getChartData() {
    return {
      labels: this.categories.map((c) => c.name),
      values: this.categories.map((c) => c.percentage),
    };
  }
}
