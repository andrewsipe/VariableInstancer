# Variable Font Instancer

Extract static font instances from variable fonts. Companion **TableEditor** defines STAT/fvar data first.

Declutter / product-pass notes: `PRODUCT_REFINEMENT_NOTES.md`.

## Scripts

### `VariableFont_Instancer.py`
Extract static instances from variable fonts.

**Naming strategies:** `stat` (default), `fvar`, `hybrid`.

```bash
python VariableFont_Instancer.py fontfile.ttf
python VariableFont_Instancer.py fonts/ -R --dry-run
python VariableFont_Instancer.py fontfile.ttf --auto --naming hybrid
python VariableFont_Instancer.py fontfile.ttf --info
```

### `VariableFont_TableEditor.py`
Define STAT axis values and fvar named instances (run **before** Instancer when you need to author tables).

```bash
python VariableFont_TableEditor.py font.ttf --info
python VariableFont_TableEditor.py font.ttf --config axes.yaml
python VariableFont_TableEditor.py font.ttf --dry-run
```

## Related

- **VarFontStudio** — macOS GUI for instance planning / export
- FontCore name policies for static-aligned variable filenames
