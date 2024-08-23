# Spotify 2023 Insights Dashboard

This project provides an interactive dashboard offering insights into the top Spotify songs of 2023. The dashboard leverages enriched datasets, visual analytics, and custom designs to provide a comprehensive overview of music trends for the year.

## Files Included

- **background.jpg**: Custom-designed background image using a glassmorphism style for the Power BI dashboard.
- **deneb heat map.json**: JSON configuration for the DENEB visual used in the project.
- **spotify-2023.csv**: The original dataset containing details about the top Spotify songs of 2023, sourced from [Kaggle](https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023?resource=download).
- **spotify.pbix**: Power BI file containing the final dashboard with all visualizations, measures, and formatting.
- **spotify.py**: Python script used to scrape the URLs for the cover and album images from Spotify.
- **spotify_tracks_with_cover_urls.csv**: Enriched dataset with additional columns for cover and album image URLs.

## Workflow

1. **Data Acquisition**:
   - The original dataset was sourced from Kaggle, providing detailed information on the top Spotify songs of 2023.
  
2. **Data Enrichment**:
   - A Python script (`spotify.py`) was written to scrape URLs for the cover and album images directly from Spotify, adding visual context to the data.
  
3. **Background Design**:
   - A custom background (`background.jpg`) was created using a glassmorphism style to enhance the visual appeal of the dashboard.

4. **Date and KPI Generation**:
   - Bravo for Power BI was used to generate date table
   - Calculated various KPIs and measures, including:
     - **Top song vs avg val**
     - **Top song vs avg**
     - **Top song stream**
     - **Percent val**
     - **Max stream**
     - **Avg stream per year**
     - **_Image html**

5. **Visualization**:
   - The enriched dataset and calculated measures were used to create various visualizations, including:
     - Bar charts
     - Line graphs
     - Cards
     - Slicers
     - DENEB visuals using the configuration in `deneb heat map.json`
     - HTML content to display cover art
  
6. **Final Output**:
   - The final dashboard (`spotify.pbix`) combines all these elements to provide a detailed and visually appealing analysis of the top Spotify songs of 2023.

## Features

- **Enriched Dataset**: Additional columns for cover and album URLs.
- **Custom Visuals**: Utilization of DENEB visuals and HTML content for dynamic presentation.
- **Custom Background**: Glassmorphism design to improve user experience.
- **Interactive Visualizations**: Includes slicers, bar charts, and line graphs for in-depth analysis.
