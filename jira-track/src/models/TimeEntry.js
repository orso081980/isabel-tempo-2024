/**
 * TimeEntry Model
 * Represents a single time tracking entry
 */
export class TimeEntry {
  constructor(data) {
    this.description = data["Work Description"] || "-";
    this.billedHours = data["Billed Hours"] || "-";
    this.workDate = data["Work date"] || "-";
  }

  getFormattedDate() {
    if (this.workDate === "-") return "-";
    const date = new Date(this.workDate);
    return date.toLocaleDateString("en-US", {
      month: "short",
      day: "numeric",
      year: "numeric",
    });
  }
}
