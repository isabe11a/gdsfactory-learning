# GDSFactory learning

Small photonic integrated-circuit layout exercises using GDSFactory and its
freely available generic demonstration PDK.

## Week 01: two straight waveguides

`week01/layout.py` builds the top cell `week01_straights` with two straight
waveguide instances. Dimensions are in micrometres:

| Instance | Length | Width | Centreline y |
| --- | ---: | ---: | ---: |
| Lower | 100 | 0.5 | 0 |
| Upper | 100 | 0.8 | 10 |

The script activates the generic PDK, creates the straight components, places
references in the top cell, and writes `week01.gds` in the working directory.
The `Component` is a cell definition; `add_ref` creates an instance in its
parent cell, and `movey` changes that instance's placement.

Milestone on 2026-10-14: the author ran this script locally and confirmed that
both waveguides were visible in the exported GDS opened in KLayout. These
nominal dimensions come from the script; dimensional measurement in KLayout
has not yet been reported.

## Run on macOS

If the existing environment is already working, keep using it. To set up a
fresh checkout, install [uv](https://docs.astral.sh/uv/getting-started/installation/)
first, then run these commands from the repository root:

```bash
cd week01
uv venv --python 3.12
uv pip install --python .venv/bin/python -r requirements.txt
.venv/bin/python layout.py
```

Using the explicit interpreter path installs packages into the same environment
that runs the script. Open the resulting `week01.gds` in KLayout using
**File → Open**.

`requirements.txt` is the supplied package snapshot from the first working
macOS environment, including `gdsfactory==9.51.0`. It has not been verified on
other platforms. The Python `klayout` package listed there and the standalone
KLayout desktop application are separate installations.

## Files

- `week01/layout.py`: source for the layout.
- `week01/requirements.txt`: captured package versions.
- `.gitignore`: excludes virtual environments, Python caches, and Finder metadata.

The generated GDS was not included in the supplied files. Regenerate it with
the command above, or add the existing local GDS alongside the source if desired.

## Official references

- [GDSFactory geometry tutorial](https://gdsfactory.github.io/gdsfactory/notebooks/00_geometry/)
- [uv Python environments](https://docs.astral.sh/uv/pip/environments/)
- [KLayout downloads](https://www.klayout.de/build.html)
