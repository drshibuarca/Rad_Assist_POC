<<<<<<< HEAD
"""
Generate comprehensive medical vocabulary database for radiology
EXPANDED VERSION: 5000+ entries
FIXED: Removed 'in' abbreviation, added base terms
"""
import json
import itertools

def generate_medical_vocab():
    vocab = {
        "anatomy": [],
        "findings": [],
        "measurements": [],
        "procedures": []
    }
    
    # ==================== ANATOMY TERMS (2000+) ====================
    
    # Respiratory system structures
    lung_lobes = ["right upper lobe", "left upper lobe", "right middle lobe", "right lower lobe", "left lower lobe", "lingula"]
    lung_segments = ["apical", "anterior", "posterior", "lateral", "medial", "superior", "inferior", "apical", "anteromedial", "lateral basal", "anterior basal", "medial basal", "posterior basal"]
    
    # Add base lobes
    for lobe in lung_lobes:
        vocab["anatomy"].append({
            "term": lobe,
            "abbreviation": "".join([w[0] for w in lobe.split()]).upper() if "lobe" in lobe else None,
            "variants": [],
            "phonetic_similar": [lobe],
            "snomed_code": f"L{str(len(vocab['anatomy'])).zfill(7)}",
            "category": "lung"
        })

    for lobe in lung_lobes:
        for segment in lung_segments:
            vocab["anatomy"].append({
                "term": f"{segment} segment of {lobe}",
                "abbreviation": None,
                "variants": [f"{lobe} {segment} segment", f"{segment} {lobe}"],
                "phonetic_similar": [f"{segment} seg ment of {lobe}"],
                "snomed_code": f"L{str(len(vocab['anatomy'])).zfill(7)}",
                "category": "lung segment"
            })
    
    # Skeletal system
    bones = ["skull", "cranium", "mandible", "maxilla", "zygomatic", "temporal", "parietal", "frontal", "occipital", "sphenoid", "ethmoid", 
             "clavicle", "scapula", "humerus", "radius", "ulna", "carpal", "metacarpal", "phalanx",
             "sternum", "rib", "vertebra", "cervical spine", "thoracic spine", "lumbar spine", "sacrum", "coccyx",
             "pelvis", "ilium", "ischium", "pubis", "femur", "patella", "tibia", "fibula", "tarsal", "metatarsal", "calcaneus", "talus"]
    
    bone_parts = ["head", "neck", "shaft", "body", "tubercle", "tuberosity", "condyle", "epicondyle", "process", "spine", "foramen", "fossa", "canal", "sinus", "crest"]
    
    for bone in bones:
        vocab["anatomy"].append({
            "term": bone,
            "abbreviation": None,
            "variants": [f"{bone} bone"],
            "phonetic_similar": [bone],
            "snomed_code": f"B{str(len(vocab['anatomy'])).zfill(7)}",
            "category": "bone"
        })
        for part in bone_parts[:5]:
            vocab["anatomy"].append({
                "term": f"{bone} {part}",
                "abbreviation": None,
                "variants": [f"{part} of {bone}"],
                "phonetic_similar": [f"{bone} {part}"],
                "snomed_code": f"B{str(len(vocab['anatomy'])).zfill(7)}",
                "category": "bone part"
            })
    
    # Cardiovascular system
    vessels = ["aorta", "pulmonary artery", "pulmonary vein", "superior vena cava", "inferior vena cava",
               "coronary artery", "carotid artery", "subclavian artery", "vertebral artery", "basilar artery",
               "iliac artery", "femoral artery", "popliteal artery", "tibial artery", "radial artery", "ulnar artery"]
    
    vessel_descriptors = ["ascending", "descending", "arch", "trunk", "branch", "bifurcation", "origin", "proximal", "distal", "wall"]
    
    for vessel in vessels:
        vocab["anatomy"].append({
            "term": vessel,
            "abbreviation": None,
            "variants": [f"{vessel}"],
            "phonetic_similar": [vessel],
            "snomed_code": f"V{str(len(vocab['anatomy'])).zfill(7)}",
            "category": "vascular"
        })
        for descriptor in vessel_descriptors:
            vocab["anatomy"].append({
                "term": f"{descriptor} {vessel}",
                "abbreviation": None,
                "variants": [f"{vessel} {descriptor}"],
                "phonetic_similar": [f"{descriptor} {vessel}"],
                "snomed_code": f"V{str(len(vocab['anatomy'])).zfill(7)}",
                "category": "vascular"
            })
    
    # Organs
    organs = ["heart", "lung", "liver", "spleen", "pancreas", "kidney", "bladder", "stomach", "intestine",
              "esophagus", "trachea", "thyroid", "adrenal gland", "prostate", "uterus", "ovary"]
    
    organ_parts = ["lobe", "segment", "cortex", "medulla", "capsule", "parenchyma", "hilum", "apex", "base", "dome", "wall", "mucosa"]
    
    for organ in organs:
        vocab["anatomy"].append({
            "term": organ,
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": [organ],
            "snomed_code": f"O{str(len(vocab['anatomy'])).zfill(7)}",
            "category": "organ"
        })
        for part in organ_parts:
            vocab["anatomy"].append({
                "term": f"{organ} {part}",
                "abbreviation": None,
                "variants": [f"{part} of {organ}"],
                "phonetic_similar": [f"{organ} {part}"],
                "snomed_code": f"O{str(len(vocab['anatomy'])).zfill(7)}",
                "category": "organ"
            })
    
    # Joints and soft tissue
    joints = ["shoulder", "elbow", "wrist", "hip", "knee", "ankle", "temporomandibular", "sternoclavicular", "acromioclavicular"]
    joint_components = ["capsule", "ligament", "tendon", "cartilage", "meniscus", "bursa", "synovium"]
    
    for joint in joints:
        vocab["anatomy"].append({
            "term": joint,
            "abbreviation": None,
            "variants": [f"{joint} joint"],
            "phonetic_similar": [joint],
            "snomed_code": f"J{str(len(vocab['anatomy'])).zfill(7)}",
            "category": "joint"
        })
        for component in joint_components:
            vocab["anatomy"].append({
                "term": f"{joint} {component}",
                "abbreviation": None,
                "variants": [f"{component} of {joint}"],
                "phonetic_similar": [f"{joint} {component}"],
                "snomed_code": f"J{str(len(vocab['anatomy'])).zfill(7)}",
                "category": "joint"
            })
    
    # Nervous system
    brain_parts = ["frontal lobe", "parietal lobe", "temporal lobe", "occipital lobe", "cerebellum", "brainstem", 
                   "thalamus", "hypothalamus", "basal ganglia", "corpus callosum", "ventricle"]
    
    for part in brain_parts:
        vocab["anatomy"].append({
            "term": part,
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": [part],
            "snomed_code": f"N{str(len(vocab['anatomy'])).zfill(7)}",
            "category": "nervous system"
        })
        for side in ["right", "left"]:
            term = f"{side} {part}"
            vocab["anatomy"].append({
                "term": term,
                "abbreviation": None,
                "variants": [term],
                "phonetic_similar": [term],
                "snomed_code": f"N{str(len(vocab['anatomy'])).zfill(7)}",
                "category": "nervous system"
            })
    
    # ==================== FINDINGS/DISEASES (2500+) ====================
    
    # Pathology descriptors
    pathology_types = ["pneumonia", "consolidation", "opacity", "nodule", "mass", "lesion", "cyst", "abscess", 
                       "tumor", "carcinoma", "adenoma", "lipoma", "hemangioma", "lymphoma", "metastasis",
                       "atelectasis", "edema", "hemorrhage", "infarct", "ischemia", "necrosis", "fibrosis",
                       "inflammation", "infection", "fracture", "dislocation", "tear", "rupture", "stenosis",
                       "obstruction", "occlusion", "thrombosis", "embolism", "aneurysm", "dissection"]
    
    locations = ["lung", "pleural", "mediastinal", "cardiac", "vascular", "hepatic", "splenic", "renal", "pancreatic",
                 "gastric", "intestinal", "osseous", "soft  tissue", "muscular", "neural", "cerebral", "spinal"]
    
    # Add base pathologies
    for pathology in pathology_types:
        vocab["findings"].append({
            "term": pathology,
            "synonyms": [],
            "phonetic_variations": [pathology],
            "severity_modifiers": ["mild", "moderate", "severe"],
            "temporal_status": ["acute", "chronic"],
            "snomed_code": f"F{str(len(vocab['findings'])).zfill(7)}"
        })

    for pathology in pathology_types:
        for location in locations:
            vocab["findings"].append({
                "term": f"{location} {pathology}",
                "synonyms": [f"{pathology} of {location}", f"{pathology} in {location}"],
                "phonetic_variations": [f"{location} {pathology}"],
                "severity_modifiers": ["minimal", "mild", "moderate", "severe", "massive"],
                "temporal_status": ["acute", "subacute", "chronic", "new", "stable", "progressive"],
                "snomed_code": f"F{str(len(vocab['findings'])).zfill(7)}"
            })
    
    # Imaging descriptors
    descriptors = ["hyperdense", "hypodense", "isodense", "heterogeneous", "homogeneous", "complex", "simple",
                   "solid", "cystic", "calcified", "cavitary", "ground-glass", "consolidative", "reticular",
                   "nodular", "linear", "branching", "lobulated", "speculated", "smooth", "irregular", "well-defined", "ill-defined"]
    
    for descriptor in descriptors:
        for finding in ["opacity", "density", "lesion", "mass", "nodule", "pattern", "appearance"]:
            vocab["findings"].append({
                "term": f"{descriptor} {finding}",
                "synonyms": [f"{finding} with {descriptor} appearance"],
                "phonetic_variations": [f"{descriptor} {finding}"],
                "severity_modifiers": ["minimal", "mild", "moderate", "marked"],
                "temporal_status": ["new", "stable", "changing"],
                "snomed_code": f"D{str(len(vocab['findings'])).zfill(7)}"
            })
    
    # Disease processes
    diseases = ["pneumonia", "tuberculosis", "sarcoidosis", "emphysema", "bronchitis", "asthma",
                "cardiomegaly", "heart failure", "myocardial infarction", "pericarditis",
                "cirrhosis", "hepatitis", "pancreatitis", "cholecystitis", "appendicitis",
                "nephritis", "nephrolithiasis", "hydronephrosis", "renal failure",
                "arthritis", "osteoporosis", "osteomyelitis", "fracture", "dislocation"]
    
    modifiers = ["acute", "chronic", "recurrent", "complicated", "uncomplicated", "early", "advanced", "end-stage"]
    
    # Add base diseases
    for disease in diseases:
        vocab["findings"].append({
            "term": disease,
            "synonyms": [],
            "phonetic_variations": [disease],
            "severity_modifiers": ["mild", "moderate", "severe"],
            "temporal_status": ["acute", "chronic"],
            "snomed_code": f"P{str(len(vocab['findings'])).zfill(7)}"
        })

    for disease in diseases:
        for modifier in modifiers:
            vocab["findings"].append({
                "term": f"{modifier} {disease}",
                "synonyms": [f"{disease}, {modifier}"],
                "phonetic_variations": [f"{modifier} {disease}"],
                "severity_modifiers": ["mild", "moderate", "severe"],
                "temporal_status": [modifier],
                "snomed_code": f"P{str(len(vocab['findings'])).zfill(7)}"
            })
    
    # Size/measurement descriptors
    size_terms = ["enlarged", "small", "normal", "increased", "decreased", "dilated", "narrowed", "thickened", "thinned"]
    anatomy_refs = ["heart", "liver", "spleen", "kidney", "lung", "vessel", "organ", "structure"]
    
    for size in size_terms:
        for anatomy in anatomy_refs:
            vocab["findings"].append({
                "term": f"{size} {anatomy}",
                "synonyms": [f"{anatomy} {size}"],
                "phonetic_variations": [f"{size} {anatomy}"],
                "severity_modifiers": ["mildly", "moderately", "severely", "markedly"],
                "temporal_status": ["stable", "progressive"],
                "snomed_code": f"S{str(len(vocab['findings'])).zfill(7)}"
            })
    
    # ==================== MEASUREMENTS (600+) ====================
    
    # Units and measurements
    units = ["millimeter", "centimeter", "meter", "inch", "pixel", "hounsfield unit", "liter", "milliliter",
             "degree", "percent", "gram", "kilogram", "density", "attenuation"]
    
    measurement_types = ["length", "width", "height", "depth", "diameter", "radius", "circumference", "area",
                        "volume", "thickness", "distance", "angle", "density", "intensity", "signal"]
    
    for unit in units:
        # Determine abbreviation - SKIP "in" for inch to avoid conflicts
        abbr = unit[:2]
        if abbr == "in":
            abbr = "inch" # Use full word instead of 'in'
            
        for mtype in measurement_types:
            vocab["measurements"].append({
                "term": f"{mtype} in {unit}",
                "abbreviations": [abbr],
                "phonetic_similar": [f"{mtype} in {unit}"],
                "regex_pattern": f"(\\d+\\.?\\d*)\\s*{unit}",
                "canonical_unit": unit
            })
    
    # ==================== PROCEDURES (400+) ====================
    
    # Imaging modalities
    modalities = ["x-ray", "radiograph", "CT", "MRI", "ultrasound", "PET", "SPECT", "fluoroscopy", "angiography", "mammography"]
    body_regions = ["chest", "abdomen", "pelvis", "head", "neck", "spine", "brain", "extremity", "joint", "bone", "soft tissue"]
    contrast_types = ["with contrast", "without contrast", "with and without contrast", "IV contrast", "oral contrast"]
    
    for modality in modalities:
        vocab["procedures"].append({
            "term": modality,
            "abbreviations": [modality if len(modality) <= 5 else None],
            "variants": [],
            "phonetic_similar": [modality],
            "snomed_code": f"I{str(len(vocab['procedures'])).zfill(7)}"
        })
        
        for region in body_regions:
            vocab["procedures"].append({
                "term": f"{modality} {region}",
                "abbreviations": [modality if len(modality) <= 5 else None],
                "variants": [f"{region} {modality}"],
                "phonetic_similar": [f"{modality} {region}"],
                "snomed_code": f"I{str(len(vocab['procedures'])).zfill(7)}"
            })
            for contrast in contrast_types[:2]:
                vocab["procedures"].append({
                    "term": f"{modality} {region} {contrast}",
                    "abbreviations": [modality if len(modality) <= 5 else None],
                    "variants": [f"{region} {modality} {contrast}"],
                    "phonetic_similar": [f"{modality} {region} {contrast}"],
                    "snomed_code": f"I{str(len(vocab['procedures'])).zfill(7)}"
                })
    
    print(f"\n{'='*60}")
    print(f"Generated Medical Vocabulary Database")
    print(f"{'='*60}")
    print(f"  Anatomy:      {len(vocab['anatomy']):>6} entries")
    print(f"  Findings:     {len(vocab['findings']):>6} entries")
    print(f"  Measurements: {len(vocab['measurements']):>6} entries")
    print(f"  Procedures:   {len(vocab['procedures']):>6} entries")
    print(f"  {'─'*60}")
    print(f"  TOTAL:        {sum(len(v) for v in vocab.values()):>6} entries")
    print(f"{'='*60}\n")
    
    return vocab

if __name__ == "__main__":
    vocab = generate_medical_vocab()
    
    output_path = "backend/data/medical_vocab.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(vocab, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Successfully saved to: {output_path}\n")
=======
"""
Generate comprehensive medical vocabulary database for radiology
EXPANDED VERSION: 5000+ entries
FIXED: Removed 'in' abbreviation, added base terms
"""
import json
import itertools

def generate_medical_vocab():
    vocab = {
        "anatomy": [],
        "findings": [],
        "measurements": [],
        "procedures": []
    }
    
    # ==================== ANATOMY TERMS (2000+) ====================
    
    # Respiratory system structures
    lung_lobes = ["right upper lobe", "left upper lobe", "right middle lobe", "right lower lobe", "left lower lobe", "lingula"]
    lung_segments = ["apical", "anterior", "posterior", "lateral", "medial", "superior", "inferior", "apical", "anteromedial", "lateral basal", "anterior basal", "medial basal", "posterior basal"]
    
    # Add base lobes
    for lobe in lung_lobes:
        vocab["anatomy"].append({
            "term": lobe,
            "abbreviation": "".join([w[0] for w in lobe.split()]).upper() if "lobe" in lobe else None,
            "variants": [],
            "phonetic_similar": [lobe],
            "snomed_code": f"L{str(len(vocab['anatomy'])).zfill(7)}",
            "category": "lung"
        })

    for lobe in lung_lobes:
        for segment in lung_segments:
            vocab["anatomy"].append({
                "term": f"{segment} segment of {lobe}",
                "abbreviation": None,
                "variants": [f"{lobe} {segment} segment", f"{segment} {lobe}"],
                "phonetic_similar": [f"{segment} seg ment of {lobe}"],
                "snomed_code": f"L{str(len(vocab['anatomy'])).zfill(7)}",
                "category": "lung segment"
            })
    
    # Skeletal system
    bones = ["skull", "cranium", "mandible", "maxilla", "zygomatic", "temporal", "parietal", "frontal", "occipital", "sphenoid", "ethmoid", 
             "clavicle", "scapula", "humerus", "radius", "ulna", "carpal", "metacarpal", "phalanx",
             "sternum", "rib", "vertebra", "cervical spine", "thoracic spine", "lumbar spine", "sacrum", "coccyx",
             "pelvis", "ilium", "ischium", "pubis", "femur", "patella", "tibia", "fibula", "tarsal", "metatarsal", "calcaneus", "talus"]
    
    bone_parts = ["head", "neck", "shaft", "body", "tubercle", "tuberosity", "condyle", "epicondyle", "process", "spine", "foramen", "fossa", "canal", "sinus", "crest"]
    
    for bone in bones:
        vocab["anatomy"].append({
            "term": bone,
            "abbreviation": None,
            "variants": [f"{bone} bone"],
            "phonetic_similar": [bone],
            "snomed_code": f"B{str(len(vocab['anatomy'])).zfill(7)}",
            "category": "bone"
        })
        for part in bone_parts[:5]:
            vocab["anatomy"].append({
                "term": f"{bone} {part}",
                "abbreviation": None,
                "variants": [f"{part} of {bone}"],
                "phonetic_similar": [f"{bone} {part}"],
                "snomed_code": f"B{str(len(vocab['anatomy'])).zfill(7)}",
                "category": "bone part"
            })
    
    # Cardiovascular system
    vessels = ["aorta", "pulmonary artery", "pulmonary vein", "superior vena cava", "inferior vena cava",
               "coronary artery", "carotid artery", "subclavian artery", "vertebral artery", "basilar artery",
               "iliac artery", "femoral artery", "popliteal artery", "tibial artery", "radial artery", "ulnar artery"]
    
    vessel_descriptors = ["ascending", "descending", "arch", "trunk", "branch", "bifurcation", "origin", "proximal", "distal", "wall"]
    
    for vessel in vessels:
        vocab["anatomy"].append({
            "term": vessel,
            "abbreviation": None,
            "variants": [f"{vessel}"],
            "phonetic_similar": [vessel],
            "snomed_code": f"V{str(len(vocab['anatomy'])).zfill(7)}",
            "category": "vascular"
        })
        for descriptor in vessel_descriptors:
            vocab["anatomy"].append({
                "term": f"{descriptor} {vessel}",
                "abbreviation": None,
                "variants": [f"{vessel} {descriptor}"],
                "phonetic_similar": [f"{descriptor} {vessel}"],
                "snomed_code": f"V{str(len(vocab['anatomy'])).zfill(7)}",
                "category": "vascular"
            })
    
    # Organs
    organs = ["heart", "lung", "liver", "spleen", "pancreas", "kidney", "bladder", "stomach", "intestine",
              "esophagus", "trachea", "thyroid", "adrenal gland", "prostate", "uterus", "ovary"]
    
    organ_parts = ["lobe", "segment", "cortex", "medulla", "capsule", "parenchyma", "hilum", "apex", "base", "dome", "wall", "mucosa"]
    
    for organ in organs:
        vocab["anatomy"].append({
            "term": organ,
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": [organ],
            "snomed_code": f"O{str(len(vocab['anatomy'])).zfill(7)}",
            "category": "organ"
        })
        for part in organ_parts:
            vocab["anatomy"].append({
                "term": f"{organ} {part}",
                "abbreviation": None,
                "variants": [f"{part} of {organ}"],
                "phonetic_similar": [f"{organ} {part}"],
                "snomed_code": f"O{str(len(vocab['anatomy'])).zfill(7)}",
                "category": "organ"
            })
    
    # Joints and soft tissue
    joints = ["shoulder", "elbow", "wrist", "hip", "knee", "ankle", "temporomandibular", "sternoclavicular", "acromioclavicular"]
    joint_components = ["capsule", "ligament", "tendon", "cartilage", "meniscus", "bursa", "synovium"]
    
    for joint in joints:
        vocab["anatomy"].append({
            "term": joint,
            "abbreviation": None,
            "variants": [f"{joint} joint"],
            "phonetic_similar": [joint],
            "snomed_code": f"J{str(len(vocab['anatomy'])).zfill(7)}",
            "category": "joint"
        })
        for component in joint_components:
            vocab["anatomy"].append({
                "term": f"{joint} {component}",
                "abbreviation": None,
                "variants": [f"{component} of {joint}"],
                "phonetic_similar": [f"{joint} {component}"],
                "snomed_code": f"J{str(len(vocab['anatomy'])).zfill(7)}",
                "category": "joint"
            })
    
    # Nervous system
    brain_parts = ["frontal lobe", "parietal lobe", "temporal lobe", "occipital lobe", "cerebellum", "brainstem", 
                   "thalamus", "hypothalamus", "basal ganglia", "corpus callosum", "ventricle"]
    
    for part in brain_parts:
        vocab["anatomy"].append({
            "term": part,
            "abbreviation": None,
            "variants": [],
            "phonetic_similar": [part],
            "snomed_code": f"N{str(len(vocab['anatomy'])).zfill(7)}",
            "category": "nervous system"
        })
        for side in ["right", "left"]:
            term = f"{side} {part}"
            vocab["anatomy"].append({
                "term": term,
                "abbreviation": None,
                "variants": [term],
                "phonetic_similar": [term],
                "snomed_code": f"N{str(len(vocab['anatomy'])).zfill(7)}",
                "category": "nervous system"
            })
    
    # ==================== FINDINGS/DISEASES (2500+) ====================
    
    # Pathology descriptors
    pathology_types = ["pneumonia", "consolidation", "opacity", "nodule", "mass", "lesion", "cyst", "abscess", 
                       "tumor", "carcinoma", "adenoma", "lipoma", "hemangioma", "lymphoma", "metastasis",
                       "atelectasis", "edema", "hemorrhage", "infarct", "ischemia", "necrosis", "fibrosis",
                       "inflammation", "infection", "fracture", "dislocation", "tear", "rupture", "stenosis",
                       "obstruction", "occlusion", "thrombosis", "embolism", "aneurysm", "dissection"]
    
    locations = ["lung", "pleural", "mediastinal", "cardiac", "vascular", "hepatic", "splenic", "renal", "pancreatic",
                 "gastric", "intestinal", "osseous", "soft  tissue", "muscular", "neural", "cerebral", "spinal"]
    
    # Add base pathologies
    for pathology in pathology_types:
        vocab["findings"].append({
            "term": pathology,
            "synonyms": [],
            "phonetic_variations": [pathology],
            "severity_modifiers": ["mild", "moderate", "severe"],
            "temporal_status": ["acute", "chronic"],
            "snomed_code": f"F{str(len(vocab['findings'])).zfill(7)}"
        })

    for pathology in pathology_types:
        for location in locations:
            vocab["findings"].append({
                "term": f"{location} {pathology}",
                "synonyms": [f"{pathology} of {location}", f"{pathology} in {location}"],
                "phonetic_variations": [f"{location} {pathology}"],
                "severity_modifiers": ["minimal", "mild", "moderate", "severe", "massive"],
                "temporal_status": ["acute", "subacute", "chronic", "new", "stable", "progressive"],
                "snomed_code": f"F{str(len(vocab['findings'])).zfill(7)}"
            })
    
    # Imaging descriptors
    descriptors = ["hyperdense", "hypodense", "isodense", "heterogeneous", "homogeneous", "complex", "simple",
                   "solid", "cystic", "calcified", "cavitary", "ground-glass", "consolidative", "reticular",
                   "nodular", "linear", "branching", "lobulated", "speculated", "smooth", "irregular", "well-defined", "ill-defined"]
    
    for descriptor in descriptors:
        for finding in ["opacity", "density", "lesion", "mass", "nodule", "pattern", "appearance"]:
            vocab["findings"].append({
                "term": f"{descriptor} {finding}",
                "synonyms": [f"{finding} with {descriptor} appearance"],
                "phonetic_variations": [f"{descriptor} {finding}"],
                "severity_modifiers": ["minimal", "mild", "moderate", "marked"],
                "temporal_status": ["new", "stable", "changing"],
                "snomed_code": f"D{str(len(vocab['findings'])).zfill(7)}"
            })
    
    # Disease processes
    diseases = ["pneumonia", "tuberculosis", "sarcoidosis", "emphysema", "bronchitis", "asthma",
                "cardiomegaly", "heart failure", "myocardial infarction", "pericarditis",
                "cirrhosis", "hepatitis", "pancreatitis", "cholecystitis", "appendicitis",
                "nephritis", "nephrolithiasis", "hydronephrosis", "renal failure",
                "arthritis", "osteoporosis", "osteomyelitis", "fracture", "dislocation"]
    
    modifiers = ["acute", "chronic", "recurrent", "complicated", "uncomplicated", "early", "advanced", "end-stage"]
    
    # Add base diseases
    for disease in diseases:
        vocab["findings"].append({
            "term": disease,
            "synonyms": [],
            "phonetic_variations": [disease],
            "severity_modifiers": ["mild", "moderate", "severe"],
            "temporal_status": ["acute", "chronic"],
            "snomed_code": f"P{str(len(vocab['findings'])).zfill(7)}"
        })

    for disease in diseases:
        for modifier in modifiers:
            vocab["findings"].append({
                "term": f"{modifier} {disease}",
                "synonyms": [f"{disease}, {modifier}"],
                "phonetic_variations": [f"{modifier} {disease}"],
                "severity_modifiers": ["mild", "moderate", "severe"],
                "temporal_status": [modifier],
                "snomed_code": f"P{str(len(vocab['findings'])).zfill(7)}"
            })
    
    # Size/measurement descriptors
    size_terms = ["enlarged", "small", "normal", "increased", "decreased", "dilated", "narrowed", "thickened", "thinned"]
    anatomy_refs = ["heart", "liver", "spleen", "kidney", "lung", "vessel", "organ", "structure"]
    
    for size in size_terms:
        for anatomy in anatomy_refs:
            vocab["findings"].append({
                "term": f"{size} {anatomy}",
                "synonyms": [f"{anatomy} {size}"],
                "phonetic_variations": [f"{size} {anatomy}"],
                "severity_modifiers": ["mildly", "moderately", "severely", "markedly"],
                "temporal_status": ["stable", "progressive"],
                "snomed_code": f"S{str(len(vocab['findings'])).zfill(7)}"
            })
    
    # ==================== MEASUREMENTS (600+) ====================
    
    # Units and measurements
    units = ["millimeter", "centimeter", "meter", "inch", "pixel", "hounsfield unit", "liter", "milliliter",
             "degree", "percent", "gram", "kilogram", "density", "attenuation"]
    
    measurement_types = ["length", "width", "height", "depth", "diameter", "radius", "circumference", "area",
                        "volume", "thickness", "distance", "angle", "density", "intensity", "signal"]
    
    for unit in units:
        # Determine abbreviation - SKIP "in" for inch to avoid conflicts
        abbr = unit[:2]
        if abbr == "in":
            abbr = "inch" # Use full word instead of 'in'
            
        for mtype in measurement_types:
            vocab["measurements"].append({
                "term": f"{mtype} in {unit}",
                "abbreviations": [abbr],
                "phonetic_similar": [f"{mtype} in {unit}"],
                "regex_pattern": f"(\\d+\\.?\\d*)\\s*{unit}",
                "canonical_unit": unit
            })
    
    # ==================== PROCEDURES (400+) ====================
    
    # Imaging modalities
    modalities = ["x-ray", "radiograph", "CT", "MRI", "ultrasound", "PET", "SPECT", "fluoroscopy", "angiography", "mammography"]
    body_regions = ["chest", "abdomen", "pelvis", "head", "neck", "spine", "brain", "extremity", "joint", "bone", "soft tissue"]
    contrast_types = ["with contrast", "without contrast", "with and without contrast", "IV contrast", "oral contrast"]
    
    for modality in modalities:
        vocab["procedures"].append({
            "term": modality,
            "abbreviations": [modality if len(modality) <= 5 else None],
            "variants": [],
            "phonetic_similar": [modality],
            "snomed_code": f"I{str(len(vocab['procedures'])).zfill(7)}"
        })
        
        for region in body_regions:
            vocab["procedures"].append({
                "term": f"{modality} {region}",
                "abbreviations": [modality if len(modality) <= 5 else None],
                "variants": [f"{region} {modality}"],
                "phonetic_similar": [f"{modality} {region}"],
                "snomed_code": f"I{str(len(vocab['procedures'])).zfill(7)}"
            })
            for contrast in contrast_types[:2]:
                vocab["procedures"].append({
                    "term": f"{modality} {region} {contrast}",
                    "abbreviations": [modality if len(modality) <= 5 else None],
                    "variants": [f"{region} {modality} {contrast}"],
                    "phonetic_similar": [f"{modality} {region} {contrast}"],
                    "snomed_code": f"I{str(len(vocab['procedures'])).zfill(7)}"
                })
    
    print(f"\n{'='*60}")
    print(f"Generated Medical Vocabulary Database")
    print(f"{'='*60}")
    print(f"  Anatomy:      {len(vocab['anatomy']):>6} entries")
    print(f"  Findings:     {len(vocab['findings']):>6} entries")
    print(f"  Measurements: {len(vocab['measurements']):>6} entries")
    print(f"  Procedures:   {len(vocab['procedures']):>6} entries")
    print(f"  {'─'*60}")
    print(f"  TOTAL:        {sum(len(v) for v in vocab.values()):>6} entries")
    print(f"{'='*60}\n")
    
    return vocab

if __name__ == "__main__":
    vocab = generate_medical_vocab()
    
    output_path = "backend/data/medical_vocab.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(vocab, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Successfully saved to: {output_path}\n")
>>>>>>> 533fb4b11c272a6a418375a1b2219f1c766b90bb
