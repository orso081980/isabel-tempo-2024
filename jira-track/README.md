# Jira Track - Professional Time Tracking Dashboard

A modern, professional Vue.js 3 application for tracking and visualizing time reports with a clean, minimal design using Tailwind CSS.

## 🚀 Features

- **Modern Architecture**: Built with Vue 3 Composition API
- **SOLID Principles**: Clean, maintainable code following best practices
- **MVC Pattern**: Proper separation of concerns with Models, Views, and Services
- **Tailwind CSS**: Utility-first CSS framework for consistent, professional design
- **Vue Chart.js**: Professional chart visualization with minimal component logic
- **Responsive**: Works seamlessly on desktop and mobile devices
- **Clean Design**: White background with purple (Isabel), red (Finca), and cyan (Freetime) accents
- **Interactive Charts**: Beautiful pie charts with proper separation of concerns

## 🎨 Design System

### Colors

- **Isabel (Purple)**: `#9333EA` - Primary brand color
- **Finca (Red)**: `#EF4444` - Secondary accent
- **Freetime (Cyan/Sea)**: `#06B6D4` - Tertiary accent
- **Background**: White with gray accents

### Typography

- **Font Family**: Inter (Google Fonts)
- **Weights**: 300, 400, 500, 600, 700, 800

## 📁 Project Structure

```
jira-track/
├── src/
│   ├── components/         # Vue components (presentation only)
│   │   ├── Dashboard.vue   # Main dashboard container
│   │   ├── TimeReportCard.vue  # Individual report card
│   │   └── PieChart.vue    # Chart visualization (minimal logic)
│   ├── composables/        # Vue composables (business logic)
│   │   ├── useTimeReports.js   # Report state management
│   │   └── useChartData.js     # Chart data preparation
│   ├── models/             # Data models
│   │   ├── TimeReport.js
│   │   └── TimeEntry.js
│   ├── services/           # Business logic & API
│   │   ├── DataService.js
│   │   └── ChartConfigService.js  # Chart configuration
│   ├── style.css           # Main CSS file (Tailwind directives)
│   ├── App.vue             # Root component
│   └── main.js             # Application entry
├── public/                 # Static assets
├── index.html              # HTML entry point
├── tailwind.config.js      # Tailwind configuration
├── postcss.config.js       # PostCSS configuration
├── vite.config.js          # Vite configuration
└── package.json            # Dependencies
```

## 🛠️ Installation & Setup

1. **Install Dependencies**

   ```bash
   cd jira-track
   npm install
   ```

2. **Run Development Server**

   ```bash
   npm run dev
   ```

3. **Build for Production**

   ```bash
   npm run build
   ```

4. **Preview Production Build**
   ```bash
   npm run preview
   ```

## 🏗️ Architecture Principles

### SOLID Principles Applied

1. **Single Responsibility Principle**
   - Each component focuses solely on presentation
   - Business logic separated into composables and services
   - `ChartConfigService` handles all chart configuration
   - `DataService` handles data fetching

2. **Open/Closed Principle**
   - Services are open for extension, closed for modification
   - Easy to add new data sources or chart types

3. **Liskov Substitution Principle**
   - Models can be extended without breaking functionality

4. **Interface Segregation Principle**
   - Composables provide specific, focused interfaces
   - `useChartData` separates chart logic from component

5. **Dependency Inversion Principle**
   - Factory functions for creating services
   - Components depend on abstractions, not concrete implementations

### Separation of Concerns

- **Components**: Pure presentation with Tailwind classes (NO custom CSS)
- **Composables**: Reusable reactive logic
- **Services**: Business logic and external dependencies
- **Models**: Data structure and domain logic
- **Style**: Single main CSS file with Tailwind directives

### CSS Architecture

- **NO scoped styles** in components
- **Tailwind utility classes** for all styling
- **Single style.css** with Tailwind directives and custom utilities
- **Custom colors** defined in Tailwind config

## 📊 Data Format

The application expects a JSON file (`tempo_report.json`) with the following structure:

```json
{
  "08-23": {
    "finca_time": 0,
    "finca_percentage": 0.0,
    "finca_data": [],
    "isabelgroup_time": 144.0,
    "isabelgroup_percentage": 100.0,
    "isabelgroup_data": [
      {
        "Work Description": "Task description",
        "Billed Hours": "8",
        "Work date": "2023-08-07 09:00"
      }
    ],
    "freetime_time": 0,
    "freetime_percentage": 0.0,
    "freetime_data": []
  }
}
```

## 🔧 Customization

### Adding New Categories

1. Update `tailwind.config.js` with new color
2. Edit `ChartConfigService.js` to add color mapping
3. Update `TimeReportCard.vue` helper methods

### Changing Data Source

Edit the factory function call in `useTimeReports.js`:

```javascript
const dataService = createDataService("your-data-source.json");
```

### Modifying Colors

Update `tailwind.config.js`:

```javascript
theme: {
  extend: {
    colors: {
      'your-category': '#HEX_COLOR',
    }
  }
}
```

## 📦 Dependencies

- **vue**: ^3.4.21
- **chart.js**: ^4.4.2
- **vue-chartjs**: Latest
- **tailwindcss**: Latest
- **vite**: ^5.2.0
- **@vitejs/plugin-vue**: ^5.0.4

## 📄 License

Built with ❤️ for professional time tracking

## 🤝 Contributing

This is a professional tool following modern Vue.js, Tailwind CSS, and software engineering best practices:

- Strict separation of concerns
- No CSS in components
- Logic-free presentation layer
- Services for all business logic
