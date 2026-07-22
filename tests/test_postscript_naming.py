import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from Variable_Instancer.VariableFont_Instancer import (  # noqa: E402
    InstanceInfo,
    FontMetadata,
    NamingMode,
    PostScriptNamingMode,
    STATNameParser,
    aggregate_postscript_stems,
    build_default_postscript_name,
    build_postscript_resolver,
    fvar_postscript_coverage,
    postscript_summary_stem,
)


def _make_inst(
    index: int,
    stat_name: str,
    coordinates: dict,
    *,
    fvar_ps_name=None,
) -> InstanceInfo:
    weight = coordinates.get("wght", 400.0)
    return InstanceInfo(
        index=index,
        fvar_name=stat_name,
        stat_name=stat_name,
        coordinates=coordinates,
        is_italic=coordinates.get("slnt", 0) != 0,
        is_bold=abs(weight - 700) < 0.5,
        fvar_ps_name=fvar_ps_name,
    )


class PostScriptNamingTests(unittest.TestCase):
    def test_postscript_summary_stem_concatenates_legacy_multi_hyphen(self):
        self.assertEqual(
            postscript_summary_stem("Playfair-Micro-SemiCondensedSemilight"),
            "PlayfairMicro-",
        )
        self.assertEqual(
            postscript_summary_stem("PlayfairMicro-SemiCondensedSemilight"),
            "PlayfairMicro-",
        )
        self.assertEqual(postscript_summary_stem("Playfair-Regular"), "Playfair-")

    def test_build_default_postscript_name(self):
        self.assertEqual(
            build_default_postscript_name("Playfair", "Micro SemiCondensed Semilight"),
            "Playfair-MicroSemiCondensedSemilight",
        )

    def test_fvar_postscript_coverage(self):
        instances = [
            _make_inst(0, "Thin", {"wght": 100}, fvar_ps_name="Playfair-Thin"),
            _make_inst(1, "Regular", {"wght": 400}, fvar_ps_name=None),
        ]
        self.assertEqual(fvar_postscript_coverage(instances), (1, 2))

    def test_aggregate_postscript_stems_preserves_order(self):
        metadata = FontMetadata(
            axes=[],
            instances=[],
            stat_values={},
            source_italic=False,
            family_name="Playfair",
        )
        stat_parser = STATNameParser.__new__(STATNameParser)
        instances = [
            _make_inst(
                0,
                "Micro SemiCondensed Semilight",
                {"opsz": 8, "wdth": 75, "wght": 350},
                fvar_ps_name="PlayfairMicro-SemiCondensedSemilight",
            ),
            _make_inst(
                1,
                "Micro SemiCondensed Semilight",
                {"opsz": 8, "wdth": 75, "wght": 400},
                fvar_ps_name="PlayfairMicro-SemiCondensedSemilight",
            ),
            _make_inst(
                2,
                "Caption SemiCondensed Semilight",
                {"opsz": 12, "wdth": 75, "wght": 350},
                fvar_ps_name="PlayfairCaption-SemiCondensedSemilight",
            ),
        ]
        resolver = build_postscript_resolver(
            metadata,
            stat_parser,
            NamingMode.STAT,
            PostScriptNamingMode.FVAR_PS,
        )
        stems = aggregate_postscript_stems(instances, resolver.resolve)
        self.assertEqual(
            stems,
            [("PlayfairMicro-", 2), ("PlayfairCaption-", 1)],
        )

    def test_fvar_ps_resolver_falls_back_to_default(self):
        metadata = FontMetadata(
            axes=[],
            instances=[],
            stat_values={},
            source_italic=False,
            family_name="Playfair",
        )
        stat_parser = STATNameParser.__new__(STATNameParser)
        inst = _make_inst(0, "Thin", {"wght": 100}, fvar_ps_name=None)
        resolver = build_postscript_resolver(
            metadata,
            stat_parser,
            NamingMode.STAT,
            PostScriptNamingMode.FVAR_PS,
        )
        ps_name, used_fvar = resolver.resolve_with_fallback_note(inst)
        self.assertFalse(used_fvar)
        self.assertEqual(ps_name, "Playfair-Thin")


if __name__ == "__main__":
    unittest.main()
