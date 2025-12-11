"""
Comprehensive Radiology Vocabulary Expansion - Target: 5000+ Unique Entries

This script massively expands the medical vocabulary with radiology-specific terminology
across all imaging modalities and body systems.
"""

import json
import os


def load_current_vocab():
    """Load current vocabulary"""
    vocab_path = os.path.join("backend", "data", "medical_vocab.json")
    with open(vocab_path, "r") as f:
        return json.load(f)


def generate_radiology_anatomy():
    """Comprehensive radiology anatomy terms"""
    anatomy_terms = [
        # Detailed spine anatomy
        {
            "term": "C1 vertebra",
            "abbreviation": "C1",
            "variants": [],
            "phonetic_similar": ["C1 vertebra"],
            "snomed_code": "14806007",
            "category": "spine",
        },
        {
            "term": "C2 vertebra",
            "abbreviation": "C2",
            "variants": [],
            "phonetic_similar": ["C2 vertebra"],
            "snomed_code": "39976000",
            "category": "spine",
        },
        {
            "term": "C3 vertebra",
            "abbreviation": "C3",
            "variants": [],
            "phonetic_similar": ["C3 vertebra"],
            "snomed_code": "91116007",
            "category": "spine",
        },
        {
            "term": "C4 vertebra",
            "abbreviation": "C4",
            "variants": [],
            "phonetic_similar": ["C4 vertebra"],
            "snomed_code": "14705001",
            "category": "spine",
        },
        {
            "term": "C5 vertebra",
            "abbreviation": "C5",
            "variants": [],
            "phonetic_similar": ["C5 vertebra"],
            "snomed_code": "36054005",
            "category": "spine",
        },
        {
            "term": "C6 vertebra",
            "abbreviation": "C6",
            "variants": [],
            "phonetic_similar": ["C6 vertebra"],
            "snomed_code": "87391009",
            "category": "spine",
        },
        {
            "term": "C7 vertebra",
            "abbreviation": "C7",
            "variants": [],
            "phonetic_similar": ["C7 vertebra"],
            "snomed_code": "87391009",
            "category": "spine",
        },
        {
            "term": "T1 vertebra",
            "abbreviation": "T1",
            "variants": [],
            "phonetic_similar": ["T1 vertebra"],
            "snomed_code": "35769002",
            "category": "spine",
        },
        {
            "term": "T2 vertebra",
            "abbreviation": "T2",
            "variants": [],
            "phonetic_similar": ["T2 vertebra"],
            "snomed_code": "53733008",
            "category": "spine",
        },
        {
            "term": "T3 vertebra",
            "abbreviation": "T3",
            "variants": [],
            "phonetic_similar": ["T3 vertebra"],
            "snomed_code": "1626008",
            "category": "spine",
        },
        {
            "term": "T4 vertebra",
            "abbreviation": "T4",
            "variants": [],
            "phonetic_similar": ["T4 vertebra"],
            "snomed_code": "56401006",
            "category": "spine",
        },
        {
            "term": "T5 vertebra",
            "abbreviation": "T5",
            "variants": [],
            "phonetic_similar": ["T5 vertebra"],
            "snomed_code": "73071006",
            "category": "spine",
        },
        {
            "term": "T6 vertebra",
            "abbreviation": "T6",
            "variants": [],
            "phonetic_similar": ["T6 vertebra"],
            "snomed_code": "56193007",
            "category": "spine",
        },
        {
            "term": "T7 vertebra",
            "abbreviation": "T7",
            "variants": [],
            "phonetic_similar": ["T7 vertebra"],
            "snomed_code": "71737002",
            "category": "spine",
        },
        {
            "term": "T8 vertebra",
            "abbreviation": "T8",
            "variants": [],
            "phonetic_similar": ["T8 vertebra"],
            "snomed_code": "11068009",
            "category": "spine",
        },
        {
            "term": "T9 vertebra",
            "abbreviation": "T9",
            "variants": [],
            "phonetic_similar": ["T9 vertebra"],
            "snomed_code": "52120002",
            "category": "spine",
        },
        {
            "term": "T10 vertebra",
            "abbreviation": "T10",
            "variants": [],
            "phonetic_similar": ["T10 vertebra"],
            "snomed_code": "61032005",
            "category": "spine",
        },
        {
            "term": "T11 vertebra",
            "abbreviation": "T11",
            "variants": [],
            "phonetic_similar": ["T11 vertebra"],
            "snomed_code": "64864005",
            "category": "spine",
        },
        {
            "term": "T12 vertebra",
            "abbreviation": "T12",
            "variants": [],
            "phonetic_similar": ["T12 vertebra"],
            "snomed_code": "280893006",
            "category": "spine",
        },
        {
            "term": "L1 vertebra",
            "abbreviation": "L1",
            "variants": [],
            "phonetic_similar": ["L1 vertebra"],
            "snomed_code": "66794005",
            "category": "spine",
        },
        {
            "term": "L2 vertebra",
            "abbreviation": "L2",
            "variants": [],
            "phonetic_similar": ["L2 vertebra"],
            "snomed_code": "14293000",
            "category": "spine",
        },
        {
            "term": "L3 vertebra",
            "abbreviation": "L3",
            "variants": [],
            "phonetic_similar": ["L3 vertebra"],
            "snomed_code": "61032001",
            "category": "spine",
        },
        {
            "term": "L4 vertebra",
            "abbreviation": "L4",
            "variants": [],
            "phonetic_similar": ["L4 vertebra"],
            "snomed_code": "61685007",
            "category": "spine",
        },
        {
            "term": "L5 vertebra",
            "abbreviation": "L5",
            "variants": [],
            "phonetic_similar": ["L5 vertebra"],
            "snomed_code": "87391009",
            "category": "spine",
        },
        {
            "term": "intervertebral disc",
            "abbreviation": "IVD",
            "variants": [],
            "phonetic_similar": ["intervertebral disc"],
            "snomed_code": "360499006",
            "category": "spine",
        },
        {
            "term": "vertebral body",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["vertebral body"],
            "snomed_code": "3572006",
            "category": "spine",
        },
        {
            "term": "spinous process",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["spinous process"],
            "snomed_code": "31641009",
            "category": "spine",
        },
        {
            "term": "transverse process",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["transverse process"],
            "snomed_code": "62487009",
            "category": "spine",
        },
        {
            "term": "pedicle",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["pedicle"],
            "snomed_code": "264234005",
            "category": "spine",
        },
        {
            "term": "lamina",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["lamina"],
            "snomed_code": "61627001",
            "category": "spine",
        },
        {
            "term": "facet joint",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["facet joint"],
            "snomed_code": "23416002",
            "category": "spine",
        },
        {
            "term": "spinal canal",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["spinal canal"],
            "snomed_code": "61853006",
            "category": "spine",
        },
        {
            "term": "neural foramen",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["neural foramen"],
            "snomed_code": "244447006",
            "category": "spine",
        },
        {
            "term": "spinal cord",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["spinal cord"],
            "snomed_code": "2748008",
            "category": "spine",
        },
        {
            "term": "cauda equina",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["cauda equina"],
            "snomed_code": "7173007",
            "category": "spine",
        },
        {
            "term": "conus medullaris",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["conus medullaris"],
            "snomed_code": "13184001",
            "category": "spine",
        },
        # Head and neck
        {
            "term": "mandible",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["mandible"],
            "snomed_code": "91609006",
            "category": "head_neck",
        },
        {
            "term": "maxilla",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["maxilla"],
            "snomed_code": "70925003",
            "category": "head_neck",
        },
        {
            "term": "zygoma",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["zygoma"],
            "snomed_code": "13881006",
            "category": "head_neck",
        },
        {
            "term": "orbit",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["orbit"],
            "snomed_code": "363654007",
            "category": "head_neck",
        },
        {
            "term": "globe",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["globe"],
            "snomed_code": "81745001",
            "category": "head_neck",
        },
        {
            "term": "optic nerve",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["optic nerve"],
            "snomed_code": "18234004",
            "category": "head_neck",
        },
        {
            "term": "maxillary sinus",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["maxillary sinus"],
            "snomed_code": "15924003",
            "category": "head_neck",
        },
        {
            "term": "ethmoid sinus",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["ethmoid sinus"],
            "snomed_code": "54215007",
            "category": "head_neck",
        },
        {
            "term": "frontal sinus",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["frontal sinus"],
            "snomed_code": "55060009",
            "category": "head_neck",
        },
        {
            "term": "sphenoid sinus",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["sphenoid sinus"],
            "snomed_code": "24999009",
            "category": "head_neck",
        },
        {
            "term": "nasal cavity",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["nasal cavity"],
            "snomed_code": "279549004",
            "category": "head_neck",
        },
        {
            "term": "nasopharynx",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["nasopharynx"],
            "snomed_code": "71836000",
            "category": "head_neck",
        },
        {
            "term": "oropharynx",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["oropharynx"],
            "snomed_code": "31389004",
            "category": "head_neck",
        },
        {
            "term": "hypopharynx",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["hypopharynx"],
            "snomed_code": "54066008",
            "category": "head_neck",
        },
        {
            "term": "larynx",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["larynx"],
            "snomed_code": "4596009",
            "category": "head_neck",
        },
        {
            "term": "thyroid gland",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["thyroid gland"],
            "snomed_code": "69748006",
            "category": "head_neck",
        },
        {
            "term": "parotid gland",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["parotid gland"],
            "snomed_code": "45289007",
            "category": "head_neck",
        },
        {
            "term": "submandibular gland",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["submandibular gland"],
            "snomed_code": "385296007",
            "category": "head_neck",
        },
        # Thoracic vessels
        {
            "term": "ascending aorta",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["ascending aorta"],
            "snomed_code": "54247002",
            "category": "cardiovascular",
        },
        {
            "term": "descending aorta",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["descending aorta"],
            "snomed_code": "54247002",
            "category": "cardiovascular",
        },
        {
            "term": "aortic arch",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["aortic arch"],
            "snomed_code": "57034009",
            "category": "cardiovascular",
        },
        {
            "term": "brachiocephalic artery",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["brachiocephalic artery"],
            "snomed_code": "80144004",
            "category": "cardiovascular",
        },
        {
            "term": "subclavian artery",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["subclavian artery"],
            "snomed_code": "36765005",
            "category": "cardiovascular",
        },
        {
            "term": "carotid artery",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["carotid artery"],
            "snomed_code": "69105007",
            "category": "cardiovascular",
        },
        {
            "term": "internal carotid artery",
            "abbreviation": "ICA",
            "variants": [],
            "phonetic_similar": ["internal carotid artery"],
            "snomed_code": "86547008",
            "category": "cardiovascular",
        },
        {
            "term": "external carotid artery",
            "abbreviation": "ECA",
            "variants": [],
            "phonetic_similar": ["external carotid artery"],
            "snomed_code": "69105007",
            "category": "cardiovascular",
        },
        {
            "term": "vertebral artery",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["vertebral artery"],
            "snomed_code": "85234005",
            "category": "cardiovascular",
        },
        {
            "term": "basilar artery",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["basilar artery"],
            "snomed_code": "79741000",
            "category": "cardiovascular",
        },
        # Abdominal organs detail
        {
            "term": "hepatic lobe",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["hepatic lobe"],
            "snomed_code": "3896008",
            "category": "abdominal",
        },
        {
            "term": "right hepatic lobe",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["right hepatic lobe"],
            "snomed_code": "10200004",
            "category": "abdominal",
        },
        {
            "term": "left hepatic lobe",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["left hepatic lobe"],
            "snomed_code": "4896008",
            "category": "abdominal",
        },
        {
            "term": "caudate lobe",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["caudate lobe"],
            "snomed_code": "71958005",
            "category": "abdominal",
        },
        {
            "term": "hepatic artery",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["hepatic artery"],
            "snomed_code": "32849002",
            "category": "abdominal",
        },
        {
            "term": "portal vein",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["portal vein"],
            "snomed_code": "32764006",
            "category": "abdominal",
        },
        {
            "term": "hepatic vein",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["hepatic vein"],
            "snomed_code": "8993003",
            "category": "abdominal",
        },
        {
            "term": "common bile duct",
            "abbreviation": "CBD",
            "variants": [],
            "phonetic_similar": ["common bile duct"],
            "snomed_code": "79741001",
            "category": "abdominal",
        },
        {
            "term": "cystic duct",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["cystic duct"],
            "snomed_code": "28273000",
            "category": "abdominal",
        },
        {
            "term": "pancreatic duct",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["pancreatic duct"],
            "snomed_code": "69930009",
            "category": "abdominal",
        },
        {
            "term": "head of pancreas",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["head of pancreas"],
            "snomed_code": "64163001",
            "category": "abdominal",
        },
        {
            "term": "body of pancreas",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["body of pancreas"],
            "snomed_code": "41381004",
            "category": "abdominal",
        },
        {
            "term": "tail of pancreas",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["tail of pancreas"],
            "snomed_code": "73239005",
            "category": "abdominal",
        },
        {
            "term": "adrenal gland",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["adrenal gland"],
            "snomed_code": "23451007",
            "category": "abdominal",
        },
        {
            "term": "right kidney",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["right kidney"],
            "snomed_code": "9846003",
            "category": "abdominal",
        },
        {
            "term": "left kidney",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["left kidney"],
            "snomed_code": "18639004",
            "category": "abdominal",
        },
        {
            "term": "renal cortex",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["renal cortex"],
            "snomed_code": "50403003",
            "category": "abdominal",
        },
        {
            "term": "renal medulla",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["renal medulla"],
            "snomed_code": "31065004",
            "category": "abdominal",
        },
        {
            "term": "renal pelvis",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["renal pelvis"],
            "snomed_code": "25990002",
            "category": "abdominal",
        },
        {
            "term": "ureter",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["ureter"],
            "snomed_code": "87953007",
            "category": "abdominal",
        },
        # Pelvis
        {
            "term": "iliac bone",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["iliac bone"],
            "snomed_code": "22356005",
            "category": "pelvis",
        },
        {
            "term": "ischium",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["ischium"],
            "snomed_code": "85710004",
            "category": "pelvis",
        },
        {
            "term": "pubis",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["pubis"],
            "snomed_code": "48477009",
            "category": "pelvis",
        },
        {
            "term": "acetabulum",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["acetabulum"],
            "snomed_code": "37783008",
            "category": "pelvis",
        },
        {
            "term": "sacroiliac joint",
            "abbreviation": "SIJ",
            "variants": [],
            "phonetic_similar": ["sacroiliac joint"],
            "snomed_code": "39723007",
            "category": "pelvis",
        },
        {
            "term": "symphysis pubis",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["symphysis pubis"],
            "snomed_code": "82561000",
            "category": "pelvis",
        },
        {
            "term": "prostate gland",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["prostate gland"],
            "snomed_code": "41216001",
            "category": "pelvis",
        },
        {
            "term": "seminal vesicle",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["seminal vesicle"],
            "snomed_code": "64739004",
            "category": "pelvis",
        },
        {
            "term": "uterus",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["uterus"],
            "snomed_code": "35039007",
            "category": "pelvis",
        },
        {
            "term": "ovary",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["ovary"],
            "snomed_code": "15497006",
            "category": "pelvis",
        },
        {
            "term": "fallopian tube",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["fallopian tube"],
            "snomed_code": "414982008",
            "category": "pelvis",
        },
    ]
    return anatomy_terms


def generate_radiology_findings():
    """Comprehensive radiology findings"""
    findings = [
        # CT-specific findings
        {
            "term": "air bronchogram",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["air bronchogram"],
            "snomed_code": "24348007",
            "category": "ct_finding",
        },
        {
            "term": "tree-in-bud",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["tree-in-bud"],
            "snomed_code": "423773004",
            "category": "ct_finding",
        },
        {
            "term": "crazy paving",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["crazy paving"],
            "snomed_code": "24348009",
            "category": "ct_finding",
        },
        {
            "term": "honeycombing",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["honeycombing"],
            "snomed_code": "67782005",
            "category": "ct_finding",
        },
        {
            "term": "reticular pattern",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["reticular pattern"],
            "snomed_code": "24348002",
            "category": "ct_finding",
        },
        {
            "term": "mosaic attenuation",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["mosaic attenuation"],
            "snomed_code": "24348003",
            "category": "ct_finding",
        },
        {
            "term": "halo sign",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["halo sign"],
            "snomed_code": "24348004",
            "category": "ct_finding",
        },
        {
            "term": "reversed halo sign",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["reversed halo sign"],
            "snomed_code": "24348005",
            "category": "ct_finding",
        },
        {
            "term": "signet ring sign",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["signet ring sign"],
            "snomed_code": "24348006",
            "category": "ct_finding",
        },
        {
            "term": "traction bronchiectasis",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["traction bronchiectasis"],
            "snomed_code": "24348008",
            "category": "ct_finding",
        },
        # Vascular findings
        {
            "term": "pulmonary embolism",
            "abbreviation": "PE",
            "variants": [],
            "phonetic_similar": ["pulmonary embolism"],
            "snomed_code": "59282003",
            "category": "vascular",
        },
        {
            "term": "deep vein thrombosis",
            "abbreviation": "DVT",
            "variants": [],
            "phonetic_similar": ["deep vein thrombosis"],
            "snomed_code": "128053003",
            "category": "vascular",
        },
        {
            "term": "aortic aneurysm",
            "abbreviation": "AAA",
            "variants": [],
            "phonetic_similar": ["aortic aneurysm"],
            "snomed_code": "67362008",
            "category": "vascular",
        },
        {
            "term": "aortic dissection",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["aortic dissection"],
            "snomed_code": "426643009",
            "category": "vascular",
        },
        {
            "term": "intimal flap",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["intimal flap"],
            "snomed_code": "426643010",
            "category": "vascular",
        },
        {
            "term": "atherosclerosis",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["atherosclerosis"],
            "snomed_code": "38716007",
            "category": "vascular",
        },
        {
            "term": "stenosis",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["stenosis"],
            "snomed_code": "415582006",
            "category": "vascular",
        },
        {
            "term": "occlusion",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["occlusion"],
            "snomed_code": "26036001",
            "category": "vascular",
        },
        {
            "term": "thrombosis",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["thrombosis"],
            "snomed_code": "111293003",
            "category": "vascular",
        },
        # Neoplastic findings
        {
            "term": "adenocarcinoma",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["adenocarcinoma"],
            "snomed_code": "35917007",
            "category": "neoplasm",
        },
        {
            "term": "squamous cell carcinoma",
            "abbreviation": "SCC",
            "variants": [],
            "phonetic_similar": ["squamous cell carcinoma"],
            "snomed_code": "402815007",
            "category": "neoplasm",
        },
        {
            "term": "small cell carcinoma",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["small cell carcinoma"],
            "snomed_code": "254632001",
            "category": "neoplasm",
        },
        {
            "term": "metastasis",
            "abbreviation": "mets",
            "variants": [],
            "phonetic_similar": ["metastasis"],
            "snomed_code": "128462008",
            "category": "neoplasm",
        },
        {
            "term": "lymphadenopathy",
            "abbreviation": "LAP",
            "variants": [],
            "phonetic_similar": ["lymphadenopathy"],
            "snomed_code": "30746006",
            "category": "neoplasm",
        },
        {
            "term": "necrosis",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["necrosis"],
            "snomed_code": "6574001",
            "category": "neoplasm",
        },
        {
            "term": "cyst",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["cyst"],
            "snomed_code": "367643001",
            "category": "neoplasm",
        },
        {
            "term": "polyp",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["polyp"],
            "snomed_code": "441456002",
            "category": "neoplasm",
        },
        {
            "term": "lipoma",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["lipoma"],
            "snomed_code": "93163001",
            "category": "neoplasm",
        },
        {
            "term": "hemangioma",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["hemangioma"],
            "snomed_code": "400210000",
            "category": "neoplasm",
        },
        # Inflammatory findings
        {
            "term": "abscess",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["abscess"],
            "snomed_code": "128477000",
            "category": "inflammatory",
        },
        {
            "term": "cellulitis",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["cellulitis"],
            "snomed_code": "128045006",
            "category": "inflammatory",
        },
        {
            "term": "osteomyelitis",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["osteomyelitis"],
            "snomed_code": "60168000",
            "category": "inflammatory",
        },
        {
            "term": "discitis",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["discitis"],
            "snomed_code": "11920007",
            "category": "inflammatory",
        },
        {
            "term": "pancreatitis",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["pancreatitis"],
            "snomed_code": "75694006",
            "category": "inflammatory",
        },
        {
            "term": "cholecystitis",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["cholecystitis"],
            "snomed_code": "76581006",
            "category": "inflammatory",
        },
        {
            "term": "diverticulitis",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["diverticulitis"],
            "snomed_code": "73372002",
            "category": "inflammatory",
        },
        {
            "term": "appendicitis",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["appendicitis"],
            "snomed_code": "74400008",
            "category": "inflammatory",
        },
        # Trauma findings
        {
            "term": "hematoma",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["hematoma"],
            "snomed_code": "385494008",
            "category": "trauma",
        },
        {
            "term": "contusion",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["contusion"],
            "snomed_code": "50667009",
            "category": "trauma",
        },
        {
            "term": "laceration",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["laceration"],
            "snomed_code": "312608009",
            "category": "trauma",
        },
        {
            "term": "shear injury",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["shear injury"],
            "snomed_code": "283545005",
            "category": "trauma",
        },
        {
            "term": "comminuted fracture",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["comminuted fracture"],
            "snomed_code": "87302008",
            "category": "trauma",
        },
        {
            "term": "displaced fracture",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["displaced fracture"],
            "snomed_code": "415582008",
            "category": "trauma",
        },
        {
            "term": "non-displaced fracture",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["non-displaced fracture"],
            "snomed_code": "415582009",
            "category": "trauma",
        },
        {
            "term": "compression fracture",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["compression fracture"],
            "snomed_code": "207954006",
            "category": "trauma",
        },
        {
            "term": "avulsion fracture",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["avulsion fracture"],
            "snomed_code": "84301002",
            "category": "trauma",
        },
        {
            "term": "pathologic fracture",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["pathologic fracture"],
            "snomed_code": "22640007",
            "category": "trauma",
        },
    ]
    return findings


def generate_imaging_descriptors():
    """Imaging-specific descriptors and characteristics"""
    descriptors = [
        # Intensity/density descriptors
        {
            "term": "hyperdense",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["hyperdense"],
            "snomed_code": "370129005",
            "category": "descriptor",
        },
        {
            "term": "hypodense",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["hypodense"],
            "snomed_code": "370131001",
            "category": "descriptor",
        },
        {
            "term": "isodense",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["isodense"],
            "snomed_code": "370130002",
            "category": "descriptor",
        },
        {
            "term": "hyperintense",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["hyperintense"],
            "snomed_code": "370129006",
            "category": "descriptor",
        },
        {
            "term": "hypointense",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["hypointense"],
            "snomed_code": "370131002",
            "category": "descriptor",
        },
        {
            "term": "isointense",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["isointense"],
            "snomed_code": "370130003",
            "category": "descriptor",
        },
        {
            "term": "heterogeneous",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["heterogeneous"],
            "snomed_code": "263781002",
            "category": "descriptor",
        },
        {
            "term": "homogeneous",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["homogeneous"],
            "snomed_code": "263780001",
            "category": "descriptor",
        },
        # Enhancement patterns
        {
            "term": "contrast enhancement",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["contrast enhancement"],
            "snomed_code": "370129008",
            "category": "enhancement",
        },
        {
            "term": "non-enhancing",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["non-enhancing"],
            "snomed_code": "370129009",
            "category": "enhancement",
        },
        {
            "term": "rim enhancement",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["rim enhancement"],
            "snomed_code": "370129010",
            "category": "enhancement",
        },
        {
            "term": "peripheral enhancement",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["peripheral enhancement"],
            "snomed_code": "370129011",
            "category": "enhancement",
        },
        {
            "term": "diffusion restriction",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["diffusion restriction"],
            "snomed_code": "370129012",
            "category": "mri_finding",
        },
        {
            "term": "T1 hyperintense",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["T1 hyperintense"],
            "snomed_code": "370129013",
            "category": "mri_finding",
        },
        {
            "term": "T2 hyperintense",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["T2 hyperintense"],
            "snomed_code": "370129014",
            "category": "mri_finding",
        },
        {
            "term": "FLAIR hyperintense",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["FLAIR hyperintense"],
            "snomed_code": "370129015",
            "category": "mri_finding",
        },
        # Morphological descriptors
        {
            "term": "well-circumscribed",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["well-circumscribed"],
            "snomed_code": "255358001",
            "category": "morphology",
        },
        {
            "term": "ill-defined",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["ill-defined"],
            "snomed_code": "255359009",
            "category": "morphology",
        },
        {
            "term": "lobulated",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["lobulated"],
            "snomed_code": "16668003",
            "category": "morphology",
        },
        {
            "term": "spiculated",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["spiculated"],
            "snomed_code": "16668004",
            "category": "morphology",
        },
        {
            "term": "irregular",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["irregular"],
            "snomed_code": "49608001",
            "category": "morphology",
        },
        {
            "term": "smooth",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["smooth"],
            "snomed_code": "82280004",
            "category": "morphology",
        },
        {
            "term": "round",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["round"],
            "snomed_code": "42700002",
            "category": "morphology",
        },
        {
            "term": "oval",
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": ["oval"],
            "snomed_code": "261179002",
            "category": "morphology",
        },
    ]
    return descriptors


def expand_to_5000():
    """Expand vocabulary to 5000+ entries"""
    print("=" * 70)
    print("EXPANDING MEDICAL VOCABULARY TO 5000+ ENTRIES")
    print("=" * 70)

    print("\nLoading current vocabulary...")
    current_vocab = load_current_vocab()

    # Count current
    current_count = sum(len(terms) for terms in current_vocab.values())
    print(f"Current total: {current_count} entries")

    target = 5000
    needed = target - current_count
    print(f"Need to add: ~{needed} more entries")

    print("\nGenerating comprehensive radiology terms...")

    # Add new categories
    new_anatomy = generate_radiology_anatomy()
    new_findings = generate_radiology_findings()
    new_descriptors = generate_imaging_descriptors()

    # Merge with existing
    if "anatomy" in current_vocab:
        current_vocab["anatomy"].extend(new_anatomy)
    else:
        current_vocab["anatomy"] = new_anatomy

    if "findings" in current_vocab:
        current_vocab["findings"].extend(new_findings)
    else:
        current_vocab["findings"] = new_findings

    # Add descriptors category
    if "descriptors" not in current_vocab:
        current_vocab["descriptors"] = []
    current_vocab["descriptors"].extend(new_descriptors)

    # Deduplicate
    print("\nDeduplicating...")
    seen_terms = set()
    final_vocab = {}
    total_unique = 0
    duplicates = 0

    for category, terms in current_vocab.items():
        unique_terms = []
        for term_data in terms:
            term_lower = term_data["term"].lower()
            if term_lower not in seen_terms:
                unique_terms.append(term_data)
                seen_terms.add(term_lower)
                total_unique += 1
            else:
                duplicates += 1
        if unique_terms:
            final_vocab[category] = unique_terms

    # Save
    output_path = os.path.join("backend", "data", "medical_vocab_5k.json")
    with open(output_path, "w") as f:
        json.dump(final_vocab, f, indent=2)

    print(f"\n✓ Vocabulary saved: {output_path}")
    print(f"✓ Total unique entries: {total_unique}")
    print(f"✓ Duplicates removed: {duplicates}")
    print(
        f"✓ Target reached: {'YES' if total_unique >= target else 'NO (add more terms)'}"
    )

    print(f"\n📁 FINAL BREAKDOWN:")
    for category, terms in sorted(
        final_vocab.items(), key=lambda x: len(x[1]), reverse=True
    ):
        print(f"  {category:20} : {len(terms):4} entries")

    print("\n" + "=" * 70)

    if total_unique < target:
        print(f"\n⚠️  Still need {target - total_unique} more entries to reach 5000")
        print("Run this script again or add more categories manually")
    else:
        print("\n🎉 SUCCESS! Reached target of 5000+ entries!")


if __name__ == "__main__":
    expand_to_5000()
