from os import listdir
from os.path import isfile, join, splitext

topics_dir_map = {
    "Astronomy, Astrophysics and Cosmology": "astro",
    "Quantum Foundations, QCQI and Applications": "qm",
    "Condensed Matter": "cm",
    "High Energy Physics": "hep",
    "Computational Pysics": "cp"
}
topics = topics_dir_map.keys()

with open("program.md", "w") as program_md:
    # Add YAML
    program_md.write(
        """---
title: Program
nav_index: 2
---

""")
    # Write Table
    program_md.write("# Program\n")
    with open("_programtable.md") as table:
        program_md.write(table.read())
    program_md.write("\n")

    # Write abstracts
    program_md.write("# Abstracts\n\n")
    for topic in topics:
        program_md.write("## "+topic+"\n\n")
        dir = join("abstracts", topics_dir_map[topic])
        files = [f for f in listdir(dir) if isfile(join(dir, f))]
        for fname in files:
            name = splitext(fname)[0]
            program_md.write("### ["+name+"](#program)\n\n")
            program_md.write(
                open(join(dir, fname)).read()
            )
            program_md.write("\n")
        program_md.write("---\n\n")
