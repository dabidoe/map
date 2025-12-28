# Campaign Map Engine

A reusable, data-driven campaign map system for tabletop RPG campaigns with integrated tactical submaps.

## Features

- 📍 **Interactive Campaign Maps** - Explore locations on real-world satellite/street maps
- ⚔️ **Tactical Submaps** - Zoom into specific locations with grid overlays for combat
- 🖼️ **Background Images** - Overlay custom floor plans or battle maps
- 👥 **Character Integration** - Link characters to locations with profile URLs
- 💾 **Save System** - Auto-save progress with export/import functionality
- 🗺️ **Multi-Campaign Support** - Swap between different campaigns easily
- 📜 **Activity Log** - Track discoveries, battles, and travel
- 📊 **Statistics** - Monitor visited locations and progress

## Quick Start

### 1. Open the Campaign Map

Open `CampaignEngine.html` in your browser. By default, it loads the American Revolution campaign.

### 2. Load a Different Campaign

To load a different campaign, edit line 570 in `CampaignEngine.html`:

```javascript
const engine = new CampaignEngine('campaigns/your-campaign.json');
```

## File Structure

```
map/
├── CampaignEngine.html          # Main campaign map engine
├── campaigns/
│   └── american-revolution.json # Campaign data (reusable format)
├── assets/
│   ├── tactical/
│   │   ├── TacticalMap.html     # Generic tactical map template
│   │   └── old-barracks-tactical.html  # Example: Old Barracks tactical map
│   └── backgrounds/             # Store map background images here
├── trenton_minimal_tacticalmapincluded.html  # Original reference file
└── campaign_map-2.html          # Original reference file
```

## Creating a New Campaign

### 1. Create Campaign JSON

Create a new file in `campaigns/your-campaign.json`:

```json
{
  "metadata": {
    "id": "your_campaign_id",
    "title": "Your Campaign Name",
    "subtitle": "Campaign tagline",
    "date": "Date or era",
    "weather": "Optional weather",
    "saveKey": "your_save_key"
  },
  "map": {
    "center": [40.7128, -74.0060],
    "zoom": 13
  },
  "locations": {
    "location-id": {
      "name": "Location Name",
      "coords": [40.7128, -74.0060],
      "elevation": 50,
      "type": "quest",
      "icon": "⚔️",
      "description": "Short description",
      "tactical": "tactical-map.html",
      "tacticalBackground": "https://url-to-background.jpg",
      "characters": ["character-id"],
      "historical": {
        "overview": "Long description",
        "facts": ["Fact 1", "Fact 2"],
        "significance": "Why this matters",
        "forces": "Forces present"
      }
    }
  },
  "characters": {
    "character-id": {
      "id": "character-id",
      "name": "Character Name",
      "title": "Their role",
      "faction": "Their faction",
      "location": "location-id",
      "profileUrl": "https://your-character-app.com/profile/123",
      "description": "About the character"
    }
  }
}
```

### 2. Location Types

Use these `type` values for color-coding:
- `quest` - Red (important objectives)
- `continental` - Blue (friendly/allied)
- `hessian` - Orange (enemy/hostile)
- `crossing` - Cyan (travel/passage)

### 3. Create Tactical Maps

#### Option A: Use the Generic Template

Link to `assets/tactical/TacticalMap.html` with URL parameters:

```json
"tactical": "TacticalMap.html?lat=40.7128&lng=-74.0060&zoom=19&background=https://image-url.jpg"
```

#### Option B: Create Custom Tactical Map

Copy `assets/tactical/old-barracks-tactical.html` and customize:
- Change coordinates and zoom in `init()`
- Add custom markers for NPCs, enemies, objectives
- Customize the legend
- Set default grid size

## Tactical Map Features

### Grid Overlay
- Toggle grid on/off
- Adjustable grid size (5ft, 10ft, 30ft, or custom)
- Labeled major grid lines for coordinate reference
- Automatically updates when map moves

### Background Images
- Overlay floor plans, battle maps, or historical images
- Adjustable opacity (0-100%)
- Images stretch to current map bounds
- Perfect for dungeon layouts or building interiors

### Map Layers
- **Street**: OpenStreetMap view
- **Satellite**: Aerial photography
- **Terrain**: Topographic map
- **Blank**: Empty canvas for custom backgrounds

## Character Integration

### Linking Characters

Add character profile URLs to integrate with external character apps:

```json
"characters": {
  "achilles": {
    "id": "achilles",
    "name": "A.G. Achilles",
    "profileUrl": "https://your-app.com/characters/achilles"
  }
}
```

### Displaying Characters

- Characters appear in the **👥 NPCs** tab
- Clicking a character jumps to their location
- Character badges show on location cards
- Profile links open in new tabs

## Save System

### Auto-Save
- Progress saves every 30 seconds
- Saves to browser localStorage
- Tracks visited locations and activity log

### Export/Import
- **Export**: Download save as JSON file
- **Import**: Load previously exported save
- Useful for sharing progress or backup

### Reset
- Clears all progress for current campaign
- Reloads the page fresh

## Advanced Features

### Route Calculator
(Planned - reference `trenton_minimal_tacticalmapincluded.html`)
- Calculate distance between locations
- Estimate travel time by foot/horse
- Visualize routes on map

### Custom Markers
Customize marker appearance in the CSS (`:root` section):
- `--accent`: Quest marker color
- Adjust `.marker-pin` classes for different styles

## Troubleshooting

### Background Images Not Loading
- Ensure CORS is allowed on image host
- Use HTTPS URLs when possible
- Check browser console for errors

### Grid Not Accurate
- Grid scale is approximate
- Works best at zoom levels 17-21
- Adjust `feetPerDegree` calculation if needed

### Save Not Persisting
- Check browser localStorage is enabled
- Different campaigns use different save keys
- Private/Incognito mode may not persist

## Examples Included

### American Revolution Campaign
- **Location**: Battle of Trenton, December 1776
- **File**: `campaigns/american-revolution.json`
- **Features**: 7 historical locations, tactical map for Old Barracks
- **Character**: A.G. Achilles (prisoner in Cell #4)

### Old Barracks Tactical Map
- **File**: `assets/tactical/old-barracks-tactical.html`
- **Features**: Satellite view, objective markers, grid overlay
- **Zoom**: Building-level detail

## Development

### Adding New Location Types
Edit CSS in `CampaignEngine.html`:

```css
.location-card.your-type { border-left-color: #your-color; }
.marker-pin.your-type { background: radial-gradient(circle, #color1, #color2); }
```

### Customizing UI
- Colors: Edit `:root` CSS variables
- Fonts: Change `font-family` values
- Layout: Adjust `.sidebar` width and positioning

## Credits

- Built on [Leaflet.js](https://leafletjs.com/)
- Map tiles: OpenStreetMap, Esri, OpenTopoMap
- Historical data: Battle of Trenton, 1776

## Future Enhancements

- [ ] Drag-and-drop token placement on tactical maps
- [ ] Real-time multiplayer support
- [ ] Fog of war / visibility system
- [ ] Encounter builder integration
- [ ] Mobile-responsive design
- [ ] Campaign timeline/calendar
- [ ] Distance/area measurement tools

## License

MIT License - Feel free to use and modify for your campaigns!

---

**Built for immersive tabletop RPG experiences.** 🎲⚔️🗺️
