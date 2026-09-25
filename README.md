[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/yusufkaraaslan-skill-seekers-badge.png)](https://mseep.ai/app/yusufkaraaslan-skill-seekers)

# Skill Seeker

[![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](https://github.com/yusufkaraaslan/Skill_Seekers/releases/tag/v2.0.0)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![MCP Integration](https://img.shields.io/badge/MCP-Integrated-blue.svg)](https://modelcontextprotocol.io)
[![Tested](https://img.shields.io/badge/Tests-379%20Passing-brightgreen.svg)](tests/)
[![Project Board](https://img.shields.io/badge/Project-Board-purple.svg)](https://github.com/users/yusufkaraaslan/projects/2)
[![PyPI version](https://badge.fury.io/py/skill-seekers.svg)](https://pypi.org/project/skill-seekers/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/skill-seekers.svg)](https://pypi.org/project/skill-seekers/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/skill-seekers.svg)](https://pypi.org/project/skill-seekers/)

**Automatically convert documentation websites, GitHub repositories, and PDFs into Claude AI skills in minutes.**

> 📋 **[View Development Roadmap & Tasks](https://github.com/users/yusufkaraaslan/projects/2)** - 134 tasks across 10 categories, pick any to contribute!

## What is Skill Seeker?

Skill Seeker is an automated tool that transforms documentation websites, GitHub repositories, and PDF files into production-ready [Claude AI skills](https://www.anthropic.com/news/skills). Instead of manually reading and summarizing documentation, Skill Seeker:

1. **Scrapes** multiple sources (docs, GitHub repos, PDFs) automatically
2. **Analyzes** code repositories with deep AST parsing
3. **Detects** conflicts between documentation and code implementation
4. **Organizes** content into categorized reference files
5. **Enhances** with AI to extract best examples and key concepts
6. **Packages** everything into an uploadable `.zip` file for Claude

**Result:** Get comprehensive Claude skills for any framework, API, or tool in 20-40 minutes instead of hours of manual work.

## Why Use This?

- 🎯 **For Developers**: Create skills from documentation + GitHub repos with conflict detection
- 🎮 **For Game Devs**: Generate skills for game engines (Godot docs + GitHub, Unity, etc.)
- 🔧 **For Teams**: Combine internal docs + code repositories into single source of truth
- 📚 **For Learners**: Build comprehensive skills from docs, code examples, and PDFs
- 🔍 **For Open Source**: Analyze repos to find documentation gaps and outdated examples

## Key Features

### 🌐 Documentation Scraping
- ✅ **llms.txt Support** - Automatically detects and uses LLM-ready documentation files (10x faster)
- ✅ **Universal Scraper** - Works with ANY documentation website
- ✅ **Smart Categorization** - Automatically organizes content by topic
- ✅ **Code Language Detection** - Recognizes Python, JavaScript, C++, GDScript, etc.
- ✅ **8 Ready-to-Use Presets** - Godot, React, Vue, Django, FastAPI, and more

### 📄 PDF Support (**v1.2.0**)
- ✅ **Basic PDF Extraction** - Extract text, code, and images from PDF files
- ✅ **OCR for Scanned PDFs** - Extract text from scanned documents
- ✅ **Password-Protected PDFs** - Handle encrypted PDFs
- ✅ **Table Extraction** - Extract complex tables from PDFs
- ✅ **Parallel Processing** - 3x faster for large PDFs
- ✅ **Intelligent Caching** - 50% faster on re-runs

### 🐙 GitHub Repository Scraping (**v2.0.0**)
- ✅ **Deep Code Analysis** - AST parsing for Python, JavaScript, TypeScript, Java, C++, Go
- ✅ **API Extraction** - Functions, classes, methods with parameters and types
- ✅ **Repository Metadata** - README, file tree, language breakdown, stars/forks
- ✅ **GitHub Issues & PRs** - Fetch open/closed issues with labels and milestones
- ✅ **CHANGELOG & Releases** - Automatically extract version history
- ✅ **Conflict Detection** - Compare documented APIs vs actual code implementation
- ✅ **MCP Integration** - Natural language: "Scrape GitHub repo facebook/react"

### 🔄 Unified Multi-Source Scraping (**NEW - v2.0.0**)
- ✅ **Combine Multiple Sources** - Mix documentation + GitHub + PDF in one skill
- ✅ **Conflict Detection** - Automatically finds discrepancies between docs and code
- ✅ **Intelligent Merging** - Rule-based or AI-powered conflict resolution
- ✅ **Transparent Reporting** - Side-by-side comparison with ⚠️ warnings
- ✅ **Documentation Gap Analysis** - Identifies outdated docs and undocumented features
- ✅ **Single Source of Truth** - One skill showing both intent (docs) and reality (code)
- ✅ **Backward Compatible** - Legacy single-source configs still work

### 🤖 AI & Enhancement
- ✅ **AI-Powered Enhancement** - Transforms basic templates into comprehensive guides
- ✅ **No API Costs** - FREE local enhancement using Claude Code Max
- ✅ **MCP Server for Claude Code** - Use directly from Claude Code with natural language

### ⚡ Performance & Scale
- ✅ **Async Mode** - 2-3x faster scraping with async/await (use `--async` flag)
- ✅ **Large Documentation Support** - Handle 10K-40K+ page docs with intelligent splitting
- ✅ **Router/Hub Skills** - Intelligent routing to specialized sub-skills
- ✅ **Parallel Scraping** - Process multiple skills simultaneously
- ✅ **Checkpoint/Resume** - Never lose progress on long scrapes
- ✅ **Caching System** - Scrape once, rebuild instantly

### ✅ Quality Assurance
- ✅ **Fully Tested** - 379 tests with comprehensive coverage

---

## 📦 Now Available on PyPI!

**Skill Seekers is now published on the Python Package Index!** Install with a single command:

```bash
pip install skill-seekers
```

Get started in seconds. No cloning, no setup - just install and run. See installation options below.

---

## Quick Start

### Option 1: Install from PyPI (Recommended)

```bash
# Install from PyPI (easiest method!)
pip install skill-seekers

# Use the unified CLI
skill-seekers scrape --config configs/react.json
skill-seekers github --repo facebook/react
skill-seekers enhance output/react/
skill-seekers package output/react/
```

**Time:** ~25 minutes | **Quality:** Production-ready | **Cost:** Free

📖 **New to Skill Seekers?** Check out our [Quick Start Guide](QUICKSTART.md) or [Bulletproof Guide](BULLETPROOF_QUICKSTART.md)

### Option 2: Install via uv (Modern Python Tool)

```bash
# Install with uv (fast, modern alternative)
uv tool install skill-seekers

# Or run directly without installing
uv tool run --from skill-seekers skill-seekers scrape --config https://raw.githubusercontent.com/yusufkaraaslan/Skill_Seekers/main/configs/react.json

# Unified CLI - simple commands
skill-seekers scrape --config configs/react.json
skill-seekers github --repo facebook/react
skill-seekers package output/react/
```

**Time:** ~25 minutes | **Quality:** Production-ready | **Cost:** Free

### Option 3: Development Install (From Source)

```bash
# Clone and install in editable mode
git clone https://github.com/yusufkaraaslan/Skill_Seekers.git
cd Skill_Seekers
pip install -e .

# Use the unified CLI
skill-seekers scrape --config configs/react.json
```

### Option 4: Use from Claude Code (MCP Integration)

```bash
# One-time setup (5 minutes)
./setup_mcp.sh

# Then in Claude Code, just ask:
"Generate a React skill from https://react.dev/"
"Scrape PDF at docs/manual.pdf and create skill"
```

**Time:** Automated | **Quality:** Production-ready | **Cost:** Free

### Option 5: Legacy CLI (Backwards Compatible)

```bash
# Install dependencies
pip3 install requests beautifulsoup4

# Run scripts directly (old method)
python3 src/skill_seekers/cli/doc_scraper.py --config configs/react.json

# Upload output/react.zip to Claude - Done!
```

**Time:** ~25 minutes | **Quality:** Production-ready | **Cost:** Free

## Usage Examples

### Documentation Scraping

```bash
# Scrape documentation website
skill-seekers scrape --config configs/react.json

# Quick scrape without config
skill-seekers scrape --url https://react.dev --name react

# With async mode (3x faster)
skill-seekers scrape --config configs/godot.json --async --workers 8
```

### Single-shot extraction (preview one page, no crawling)

```bash
# Preview what a full scrape would capture from one page
skill-seekers extract --url https://react.dev/learn --format markdown

# Save to file, or get JSON for scripting
skill-seekers extract --url https://react.dev/learn -o intro.md
skill-seekers extract --url https://react.dev/learn --format json

# Local HTML file or PDF
skill-seekers extract --file page.html --selector article
skill-seekers extract --pdf docs/manual.pdf -o manual.md
```

**Time:** seconds | **Quality:** Same extraction engine as `scrape` | **Cost:** Free
Use it to validate selectors and content quality *before* committing to a 20-40 minute scrape. Also available in Claude Code via the `extract_content` MCP tool.

### PDF Extraction

```bash
# Basic PDF extraction
skill-seekers pdf --pdf docs/manual.pdf --name myskill

# Advanced features
skill-seekers pdf --pdf docs/manual.pdf --name myskill \
    --extract-tables \        # Extract tables
    --parallel \              # Fast parallel processing
    --workers 8               # Use 8 CPU cores

# Scanned PDFs (requires: pip install pytesseract Pillow)
skill-seekers pdf --pdf docs/scanned.pdf --name myskill --ocr

# Password-protected PDFs
skill-seekers pdf --pdf docs/encrypted.pdf --name myskill --password mypassword
```

**Time:** ~5-15 minutes (or 2-5 minutes with parallel) | **Quality:** Production-ready | **Cost:** Free

### GitHub Repository Scraping

```bash
# Basic repository scraping
skill-seekers github --repo facebook/react

# Using a config file
skill-seekers github --config configs/react_github.json

# With authentication (higher rate limits)
export GITHUB_TOKEN=ghp_your_token_here
skill-seekers github --repo facebook/react

# Customize what to include
skill-seekers github --repo django/django \
    --include-issues \        # Extract GitHub Issues
    --max-issues 100 \        # Limit issue count
    --include-changelog \     # Extract CHANGELOG.md
    --include-releases        # Extract GitHub Releases
```

**Time:** ~5-10 minutes | **Quality:** Production-ready | **Cost:** Free

### Unified Multi-Source Scraping (**NEW - v2.0.0**)

**The Problem:** Documentation and code often drift apart. Docs might be outdated, missing features that exist in code, or documenting features that were removed.

**The Solution:** Combine documentation + GitHub + PDF into one unified skill that shows BOTH what's documented AND what actually exists, with clear warnings about discrepancies.

```bash
# Use existing unified configs
skill-seekers unified --config configs/react_unified.json
skill-seekers unified --config configs/django_unified.json

# Or create unified config (mix documentation + GitHub)
cat > configs/myframework_unified.json << 'EOF'
{
  "name": "myframework",
  "description": "Complete framework knowledge from docs + code",
  "merge_mode": "rule-based",
  "sources": [
    {
      "type": "documentation",
      "base_url": "https://docs.myframework.com/",
      "extract_api": true,
      "max_pages": 200
    },
    {
      "type": "github",
      "repo": "owner/myframework",
      "include_code": true,
      "code_analysis_depth": "surface"
    }
  ]
}
EOF

# Run unified scraper
skill-seekers unified --config configs/myframework_unified.json

# Package and upload
skill-seekers package output/myframework/
# Upload output/myframework.zip to Claude - Done!
```

**Time:** ~30-45 minutes | **Quality:** Production-ready with conflict detection | **Cost:** Free

**What Makes It Special:**

✅ **Conflict Detection** - Automatically finds 4 types of discrepancies:
- 🔴 **Missing in code** (high): Documented but not implemented
- 🟡 **Missing in docs** (medium): Implemented but not documented
- ⚠️ **Signature mismatch**: Different parameters/types
- ℹ️ **Description mismatch**: Different explanations

✅ **Transparent Reporting** - Shows both versions side-by-side:
```markdown
#### `move_local_x(delta: float)`

⚠️ **Conflict**: Documentation signature differs from implementation

**Documentation says:**
```
def move_local_x(delta: float)
```

**Code implementation:**
```python
def move_local_x(delta: float, snap: bool = False) -> None
```
```

✅ **Advantages:**
- **Identifies documentation gaps** - Find outdated or missing docs automatically
- **Catches code changes** - Know when APIs change without docs being updated
- **Single source of truth** - One skill showing intent (docs) AND reality (code)
- **Actionable insights** - Get suggestions for fixing each conflict
- **Development aid** - See what's actually in the codebase vs what's documented

**Example Unified Configs:**
- `configs/react_unified.json` - React docs + GitHub repo
- `configs/django_unified.json` - Django docs + GitHub repo
- `configs/fastapi_unified.json` - FastAPI docs + GitHub repo

**Full Guide:** See [docs/UNIFIED_SCRAPING.md](docs/UNIFIED_SCRAPING.md) for complete documentation.

## How It Works

```mermaid
graph LR
    A[Documentation Website] --> B[Skill Seeker]
    B --> C[Scraper]
    B --> D[AI Enhancement]
    B --> E[Packager]
    C --> F[Organized References]
    D --> F
    F --> E
    E --> G[Claude Skill .zip]
    G --> H[Upload to Claude AI]
```

0. **Detect llms.txt** - Checks for llms-full.txt, llms.txt, llms-small.txt first
1. **Scrape**: Extracts all pages from documentation
2. **Categorize**: Organizes content into topics (API, guides, tutorials, etc.)
3. **Enhance**: AI analyzes docs and creates comprehensive SKILL.md with examples
4. **Package**: Bundles everything into a Claude-ready `.zip` file

## 📋 Prerequisites

**Before you start, make sure you have:**

1. **Python 3.10 or higher** - [Download](https://www.python.org/downloads/) | Check: `python3 --version`
2. **Git** - [Download](https://git-scm.com/) | Check: `git --version`
3. **15-30 minutes** for first-time setup

**First time user?** → **[Start Here: Bulletproof Quick Start Guide](BULLETPROOF_QUICKSTART.md)** 🎯

This guide walks you through EVERYTHING step-by-step (Python install, git clone, first skill creation).

---

## 🚀 Quick Start

### Method 1: MCP Server for Claude Code (Easiest)

Use Skill Seeker directly from Claude Code with natural language!

```bash
# Clone repository
git clone https://github.com/yusufkaraaslan/Skill_Seekers.git
cd Skill_Seekers

# One-time setup (5 minutes)
./setup_mcp.sh

# Restart Claude Code, then just ask:
```

**In Claude Code:**
```
List all available configs
Generate config for Tailwind at https://tailwindcss.com/docs
Scrape docs using configs/react.json
Package skill at output/react/
```

**Benefits:**
- ✅ No manual CLI commands
- ✅ Natural language interface
- ✅ Integrated with your workflow
- ✅ 9 tools available instantly (includes automatic upload!)
- ✅ **Tested and working** in production

**Full guides:**
- 📘 [MCP Setup Guide](docs/MCP_SETUP.md) - Complete installation instructions
- 🧪 [MCP Testing Guide](docs/TEST_MCP_IN_CLAUDE_CODE.md) - Test all 9 tools
- 📦 [Large Documentation Guide](docs/LARGE_DOCUMENTATION.md) - Handle 10K-40K+ pages
- 📤 [Upload Guide](docs/UPLOAD_GUIDE.md) - How to upload skills to Claude

### Method 2: CLI (Traditional)

#### One-Time Setup: Create Virtual Environment

```bash
# Clone repository
git clone https://github.com/yusufkaraaslan/Skill_Seekers.git
cd Skill_Seekers

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # macOS/Linux
# OR on Windows: venv\Scripts\activate

# Install dependencies
pip install requests beautifulsoup4 pytest

# Save dependencies
pip freeze > requirements.txt

# Optional: Install anthropic for API-based enhancement (not needed for LOCAL enhancement)
# pip install anthropic
```

**Always activate the virtual environment before using Skill Seeker:**
```bash
source venv/bin/activate  # Run this each time you start a new terminal session
```

#### Easiest: Use a Preset

```bash
# Make sure venv is activated (you should see (venv) in your prompt)
source venv/bin/activate

# Optional: Estimate pages first (fast, 1-2 minutes)
skill-seekers estimate configs/godot.json

# Use Godot preset
skill-seekers scrape --config configs/godot.json

# Use React preset
skill-seekers scrape --config configs/react.json

# See all presets
ls configs/
```

### Interactive Mode

```bash
skill-seekers scrape --interactive
```

### Quick Mode

```bash
skill-seekers scrape \
  --name react \
  --url https://react.dev/ \
  --description "React framework for UIs"
```

## 📤 Uploading Skills to Claude

Once your skill is packaged, you need to upload it to Claude:

### Option 1: Automatic Upload (API-based)

```bash
# Set your API key (one-time)
export ANTHROPIC_API_KEY=sk-ant-...

# Package and upload automatically
skill-seekers package output/react/ --upload

# OR upload existing .zip
skill-seekers upload output/react.zip
```

**Benefits:**
- ✅ Fully automatic
- ✅ No manual steps
- ✅ Works from command line

**Requirements:**
- Anthropic API key (get from https://console.anthropic.com/)

### Option 2: Manual Upload (No API Key)

```bash
# Package skill
skill-seekers package output/react/

# This will:
# 1. Create output/react.zip
# 2. Open the output/ folder automatically
# 3. Show upload instructions

# Then manually upload:
# - Go to https://claude.ai/skills
# - Click "Upload Skill"
# - Select output/react.zip
# - Done!
```

**Benefits:**
- ✅ No API key needed
- ✅ Works for everyone
- ✅ Folder opens automatically

### Option 3: Claude Code (MCP) - Smart & Automatic

```
In Claude Code, just ask:
"Package and upload the React skill"

# With API key set:
# - Packages the skill
# - Uploads to Claude automatically
# - Done! ✅

# Without API key:
# - Packages the skill
# - Shows where to find the .zip
# - Provides manual upload instructions
```

**Benefits:**
- ✅ Natural language
- ✅ Smart auto-detection (uploads if API key available)
- ✅ Works with or without API key
- ✅ No errors or failures

---

## 📁 Simple Structure

```
doc-to-skill/
├── cli/
│   ├── doc_scraper.py      # Main scraping tool
│   ├── package_skill.py    # Package to .zip
│   ├── upload_skill.py     # Auto-upload (API)
│   └── enhance_skill.py    # AI enhancement
├── mcp/                    # MCP server for Claude Code
│   └── server.py           # 9 MCP tools
├── configs/                # Preset configurations
│   ├── godot.json         # Godot Engine
│   ├── react.json         # React
│   ├── vue.json           # Vue.js
│   ├── django.json        # Django
│   └── fastapi.json       # FastAPI
└── output/                 # All output (auto-created)
    ├── godot_data/        # Scraped data
    ├── godot/             # Built skill
    └── godot.zip          # Packaged skill
```

## ✨ Features

### 1. Fast Page Estimation (NEW!)

```bash
skill-seekers estimate configs/react.json

# Output:
📊 ESTIMATION RESULTS
✅ Pages Discovered: 180
📈 Estimated Total: 230
⏱️  Time Elapsed: 1.2 minutes
💡 Recommended max_pages: 280
```

**Benefits:**
- Know page count BEFORE scraping (saves time)
- Validates URL patterns work correctly
- Estimates total scraping time
- Recommends optimal `max_pages` setting
- Fast (1-2 minutes vs 20-40 minutes full scrape)

### 2. Auto-Detect Existing Data

```bash
skill-seekers scrape --config configs/godot.json

# If data exists:
✓ Found existing data: 245 pages
Use existing data? (y/n): y
⏭️  Skipping scrape, using existing data
```

### 3. Knowledge Generation

**Automatic pattern extraction:**
- Extracts common code patterns from docs
- Detects programming language
- Creates quick reference with real examples
- Smarter categorization with scoring

**Enhanced SKILL.md:**
- Real code examples from documentation
- Language-annotated code blocks
- Common patterns section
- Quick reference from actual usage examples

### 4. Smart Categorization

Automatically infers categories from:
- URL structure
- Page titles
- Content keywords
- With scoring for better accuracy

### 5. Code Language Detection

```python
# Automatically detects:
- Python (def, import, from)
- JavaScript (const, let, =>)
- GDScript (func, var, extends)
- C++ (#include, int main)
- And more...
```

### 5. Skip Scraping

```bash
# Scrape once
skill-seekers scrape --config configs/react.json

# Later, just rebuild (instant)
skill-seekers scrape --config configs/react.json --skip-scrape
```

### 6. Async Mode for Faster Scraping (2-3x Speed!)

```bash
# Enable async mode with 8 workers (recommended for large docs)
skill-seekers scrape --config configs/react.json --async --workers 8

# Small docs (~100-500 pages)
skill-seekers scrape --config configs/mydocs.json --async --workers 4

# Large docs (2000+ pages) with no rate limiting
skill-seekers scrape --config configs/largedocs.json --async --workers 8 --no-rate-limit
```

**Performance Comparison:**
- **Sync mode (threads):** ~18 pages/sec, 120 MB memory
- **Async mode:** ~55 pages/sec, 40 MB memory
- **Result:** 3x faster, 66% less memory!

**When to use:**
- ✅ Large documentation (500+ pages)
- ✅ Network latency is high
- ✅ Memory is constrained
- ❌ Small docs (< 100 pages) - overhead not worth it

**See full guide:** [ASYNC_SUPPORT.md](ASYNC_SUPPORT.md)

### 7. AI-Powered SKILL.md Enhancement

```bash
# Option 1: During scraping (API-based, requires API key)
pip3 install anthropic
export ANTHROPIC_API_KEY=sk-ant-...
skill-seekers scrape --config configs/react.json --enhance

# Option 2: During scraping (LOCAL, no API key - uses Claude Code Max)
skill-seekers scrape --config configs/react.json --enhance-local

# Option 3: After scraping (API-based, standalone)
skill-seekers enhance output/react/

# Option 4: After scraping (LOCAL, no API key, standalone)
skill-seekers enhance output/react/
```

**What it does:**
- Reads your reference documentation
- Uses Claude to generate an excellent SKILL.md
- Extracts best code examples (5-10 practical examples)
- Creates comprehensive quick reference
- Adds domain-specific key concepts
- Provides navigation guidance for different skill levels
- Automatically backs up original
- **Quality:** Transforms 75-line templates into 500+ line comprehensive guides

**LOCAL Enhancement (Recommended):**
- Uses your Claude Code Max plan (no API costs)
- Opens new terminal with Claude Code
- Analyzes reference files automatically
- Takes 30-60 seconds
- Quality: 9/10 (comparable to API version)

### 7. Large Documentation Support (10K-40K+ Pages)

**For massive documentation sites like Godot (40K pages), AWS, or Microsoft Docs:**

```bash
# 1. Estimate first (discover page count)
skill-seekers estimate configs/godot.json

# 2. Auto-split into focused sub-skills
python3 -m skill_seekers.cli.split_config configs/godot.json --strategy router

# Creates:
# - godot-scripting.json (5K pages)
# - godot-2d.json (8K pages)
# - godot-3d.json (10K pages)
# - godot-physics.json (6K pages)
# - godot-shaders.json (11K pages)

# 3. Scrape all in parallel (4-8 hours instead of 20-40!)
for config in configs/godot-*.json; do
  skill-seekers scrape --config $config &
done
wait

# 4. Generate intelligent router/hub skill
python3 -m skill_seekers.cli.generate_router configs/godot-*.json

# 5. Package all skills
python3 -m skill_seekers.cli.package_multi output/godot*/

# 6. Upload all .zip files to Claude
# Users just ask questions naturally!
# Router automatically directs to the right sub-skill!
```

**Split Strategies:**
- **auto** - Intelligently detects best strategy based on page count
- **category** - Split by documentation categories (scripting, 2d, 3d, etc.)
- **router** - Create hub skill + specialized sub-skills (RECOMMENDED)
- **size** - Split every N pages (for docs without clear categories)

**Benefits:**
- ✅ Faster scraping (parallel execution)
- ✅ More focused skills (better Claude performance)
- ✅ Easier maintenance (update one topic at a time)
- ✅ Natural user experience (router handles routing)
- ✅ Avoids context window limits

**Configuration:**
```json
{
  "name": "godot",
  "max_pages": 40000,
  "split_strategy": "router",
  "split_config": {
    "target_pages_per_skill": 5000,
    "create_router": true,
    "split_by_categories": ["scripting", "2d", "3d", "physics"]
  }
}
```

**Full Guide:** [Large Documentation Guide](docs/LARGE_DOCUMENTATION.md)

### 8. Checkpoint/Resume for Long Scrapes

**Never lose progress on long-running scrapes:**

```bash
# Enable in config
{
  "checkpoint": {
    "enabled": true,
    "interval": 1000  // Save every 1000 pages
  }
}

# If scrape is interrupted (Ctrl+C or crash)
skill-seekers scrape --config configs/godot.json --resume

# Resume from last checkpoint
✅ Resuming from checkpoint (12,450 pages scraped)
⏭️  Skipping 12,450 already-scraped pages
🔄 Continuing from where we left off...

# Start fresh (clear checkpoint)
skill-seekers scrape --config configs/godot.json --fresh
```

**Benefits:**
- ✅ Auto-saves every 1000 pages (configurable)
- ✅ Saves on interruption (Ctrl+C)
- ✅ Resume with `--resume` flag
- ✅ Never lose hours of scraping progress

## 🎯 Complete Workflows

### First Time (With Scraping + Enhancement)

```bash
# 1. Scrape + Build + AI Enhancement (LOCAL, no API key)
skill-seekers scrape --config configs/godot.json --enhance-local

# 2. Wait for new terminal to close (enhancement completes)
# Check the enhanced SKILL.md:
cat output/godot/SKILL.md

# 3. Package
skill-seekers package output/godot/

# 4. Done! You have godot.zip with excellent SKILL.md
```

**Time:** 20-40 minutes (scraping) + 60 seconds (enhancement) = ~21-41 minutes

### Using Existing Data (Fast!)

```bash
# 1. Use cached data + Local Enhancement
skill-seekers scrape --config configs/godot.json --skip-scrape
skill-seekers enhance output/godot/

# 2. Package
skill-seekers package output/godot/

# 3. Done!
```

**Time:** 1-3 minutes (build) + 60 seconds (enhancement) = ~2-4 minutes total

### Without Enhancement (Basic)

```bash
# 1. Scrape + Build (no enhancement)
skill-seekers scrape --config configs/godot.json

# 2. Package
skill-seekers package output/godot/

# 3. Done! (SKILL.md will be basic template)
```

**Time:** 20-40 minutes
**Note:** SKILL.md will be generic - enhancement strongly recommended!

## 📋 Available Presets

| Config | Framework | Description |
|--------|-----------|-------------|
| `godot.json` | Godot Engine | Game development |
| `react.json` | React | UI framework |
| `vue.json` | Vue.js | Progressive framework |
| `django.json` | Django | Python web framework |
| `fastapi.json` | FastAPI | Modern Python API |
| `ansible-core.json` | Ansible Core 2.19 | Automation & configuration |

### Using Presets

```bash
# Godot
skill-seekers scrape --config configs/godot.json

# React
skill-seekers scrape --config configs/react.json

# Vue
skill-seekers scrape --config configs/vue.json

# Django
skill-seekers scrape --config configs/django.json

# FastAPI
skill-seekers scrape --config configs/fastapi.json

# Ansible
skill-seekers scrape --config configs/ansible-core.json
```

## 🎨 Creating Your Own Config

### Option 1: Interactive

```bash
skill-seekers scrape --interactive
# Follow prompts, it will create the config for you
```

### Option 2: Copy and Edit

```bash
# Copy a preset
cp configs/react.json configs/myframework.json

# Edit it
nano configs/myframework.json

# Use it
skill-seekers scrape --config configs/myframework.json
```

### Config Structure

```json
{
  "name": "myframework",
  "description": "When to use this skill",
  "base_url": "https://docs.myframework.com/",
  "selectors": {
    "main_content": "article",
    "title": "h1",
    "code_blocks": "pre code"
  },
  "url_patterns": {
    "include": ["/docs", "/guide"],
    "exclude": ["/blog", "/about"]
  },
  "categories": {
    "getting_started": ["intro", "quickstart"],
    "api": ["api", "reference"]
  },
  "rate_limit": 0.5,
  "max_pages": 500
}
```

## 📊 What Gets Created

```
output/
├── godot_data/              # Scraped raw data
│   ├── pages/              # JSON files (one per page)
│   └── summary.json        # Overview
│
└── godot/                   # The skill
    ├── SKILL.md            # Enhanced with real examples
    ├── references/         # Categorized docs
    │   ├── index.md
    │   ├── getting_started.md
    │   ├── scripting.md
    │   └── ...
    ├── scripts/            # Empty (add your own)
    └── assets/             # Empty (add your own)
```

## 🎯 Command Line Options

```bash
# Interactive mode
skill-seekers scrape --interactive

# Use config file
skill-seekers scrape --config configs/godot.json

# Quick mode
skill-seekers scrape --name react --url https://react.dev/

# Skip scraping (use existing data)
skill-seekers scrape --config configs/godot.json --skip-scrape

# With description
skill-seekers scrape \
  --name react \
  --url https://react.dev/ \
  --description "React framework for building UIs"
```

## 💡 Tips

### 1. Test Small First

Edit `max_pages` in config to test:
```json
{
  "max_pages": 20  // Test with just 20 pages
}
```

### 2. Reuse Scraped Data

```bash
# Scrape once
skill-seekers scrape --config configs/react.json

# Rebuild multiple times (instant)
skill-seekers scrape --config configs/react.json --skip-scrape
skill-seekers scrape --config configs/react.json --skip-scrape
```

### 3. Finding Selectors

```python
# Test in Python
from bs4 import BeautifulSoup
import requests

url = "https://docs.example.com/page"
soup = BeautifulSoup(requests.get(url).content, 'html.parser')

# Try different selectors
print(soup.select_one('article'))
print(soup.select_one('main'))
print(soup.select_one('div[role="main"]'))
```

### 4. Check Output Quality

```bash
# After building, check:
cat output/godot/SKILL.md  # Should have real examples
cat output/godot/references/index.md  # Categories
```

## 🐛 Troubleshooting

### No Content Extracted?
- Check your `main_content` selector
- Try: `article`, `main`, `div[role="main"]`

### Data Exists But Won't Use It?
```bash
# Force re-scrape
rm -rf output/myframework_data/
skill-seekers scrape --config configs/myframework.json
```

### Categories Not Good?
Edit the config `categories` section with better keywords.

### Want to Update Docs?
```bash
# Delete old data
rm -rf output/godot_data/

# Re-scrape
skill-seekers scrape --config configs/godot.json
```

## 📈 Performance

| Task | Time | Notes |
|------|------|-------|
| Scraping (sync) | 15-45 min | First time only, thread-based |
| Scraping (async) | 5-15 min | 2-3x faster with --async flag |
| Building | 1-3 min | Fast! |
| Re-building | <1 min | With --skip-scrape |
| Packaging | 5-10 sec | Final zip |

## ✅ Summary

**One tool does everything:**
1. ✅ Scrapes documentation
2. ✅ Auto-detects existing data
3. ✅ Generates better knowledge
4. ✅ Creates enhanced skills
5. ✅ Works with presets or custom configs
6. ✅ Supports skip-scraping for fast iteration

**Simple structure:**
- `doc_scraper.py` - The tool
- `configs/` - Presets
- `output/` - Everything else

**Better output:**
- Real code examples with language detection
- Common patterns extracted from docs
- Smart categorization
- Enhanced SKILL.md with actual examples

## 📚 Documentation

### Getting Started
- **[BULLETPROOF_QUICKSTART.md](BULLETPROOF_QUICKSTART.md)** - 🎯 **START HERE** if you're new!
- **[QUICKSTART.md](QUICKSTART.md)** - Quick start for experienced users
- **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** - Common issues and solutions

### Guides
- **[docs/LARGE_DOCUMENTATION.md](docs/LARGE_DOCUMENTATION.md)** - Handle 10K-40K+ page docs
- **[ASYNC_SUPPORT.md](ASYNC_SUPPORT.md)** - Async mode guide (2-3x faster scraping)
- **[docs/ENHANCEMENT.md](docs/ENHANCEMENT.md)** - AI enhancement guide
- **[docs/TERMINAL_SELECTION.md](docs/TERMINAL_SELECTION.md)** - Configure terminal app for local enhancement
- **[docs/UPLOAD_GUIDE.md](docs/UPLOAD_GUIDE.md)** - How to upload skills to Claude
- **[docs/MCP_SETUP.md](docs/MCP_SETUP.md)** - MCP integration setup

### Technical
- **[docs/CLAUDE.md](docs/CLAUDE.md)** - Technical architecture
- **[STRUCTURE.md](STRUCTURE.md)** - Repository structure

## 🎮 Ready?

```bash
# Try Godot
skill-seekers scrape --config configs/godot.json

# Try React
skill-seekers scrape --config configs/react.json

# Or go interactive
skill-seekers scrape --interactive
```

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details

---

Happy skill building! 🚀
