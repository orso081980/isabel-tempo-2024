/**
 * DataService
 * Handles data fetching and transformation
 * Follows Single Responsibility and Open/Closed Principles
 */
import { TimeReport } from "../models/TimeReport.js";

export class DataService {
  constructor(dataSource) {
    this.dataSource = dataSource;
  }

  async fetchReports() {
    try {
      const response = await fetch(this.dataSource);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json();
      return this.transformData(data);
    } catch (error) {
      console.error("Error fetching reports:", error);
      throw error;
    }
  }

  transformData(rawData) {
    const reports = [];
    for (const [month, data] of Object.entries(rawData)) {
      reports.push(new TimeReport(month, data));
    }
    return reports;
  }
}

// Factory function following Dependency Inversion Principle
export function createDataService(dataSource = "../tempo_report.json") {
  return new DataService(dataSource);
}
