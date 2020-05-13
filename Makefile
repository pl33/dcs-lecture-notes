
BUILD_DIR = build

LATEXMK = latexmk -pdf -silent -synctex=1
LATEXMK_PVC = $(LATEXMK) -pvc

ALL_CHAPTERS = $(BUILD_DIR)/chapter00.pdf $(BUILD_DIR)/chapter01.pdf $(BUILD_DIR)/chapter02.pdf $(BUILD_DIR)/chapter03.pdf
ALL_EXERCISES = $(BUILD_DIR)/exercise00.pdf $(BUILD_DIR)/exercise01.pdf $(BUILD_DIR)/exercise02.pdf
ALL_SVGS = $(BUILD_DIR)/svg/ch01_EM_Spectrum_Properties.pdf $(BUILD_DIR)/svg/ch01_Electromagnetic-Spectrum.pdf $(BUILD_DIR)/svg/ch01_NetworkTopologies.pdf
COMMON_DEPS = common/settings.tex common/titlepage.tex common/acronym.tex common/imprint.tex DCS.bib

all: chapters exercises complete

.PHONY: chapters
chapters: $(ALL_CHAPTERS)

.PHONY: exercises
exercises: $(ALL_EXERCISES)

.PHONY: complete
complete: $(BUILD_DIR)/DCS.pdf

clean:
	mkdir -p $(BUILD_DIR)
	cd $(BUILD_DIR) ; rm -f *.aux *.fdb_latexmk *.fls *.lof *.log *.lot *.pdf *.synctex.gz

$(BUILD_DIR)/DCS.pdf: main/DCS.tex $(COMMON_DEPS) */*.tex $(ALL_SVGS)
	mkdir -p $(BUILD_DIR)
	cd $(BUILD_DIR) ; $(LATEXMK) ../$<

$(BUILD_DIR)/%.pdf: main/%.tex $(COMMON_DEPS) %/*.tex $(ALL_SVGS)
	mkdir -p $(BUILD_DIR)
	cd $(BUILD_DIR) ; $(LATEXMK) ../$<

$(BUILD_DIR)/svg/%.pdf:
	mkdir -p $(BUILD_DIR)/svg
	inkscape -D -z --file=$< --export-pdf=$@

$(BUILD_DIR)/svg_latex/%.pdf:
	mkdir -p $(BUILD_DIR)/svg_latex
	inkscape -D -z --file=$< --export-pdf=$@ --export-latex

$(BUILD_DIR)/svg/ch01_EM_Spectrum_Properties.pdf: chapter01/EM_Spectrum_Properties_edit.svg
$(BUILD_DIR)/svg/ch01_Electromagnetic-Spectrum.pdf: chapter01/Electromagnetic-Spectrum.svg
$(BUILD_DIR)/svg/ch01_NetworkTopologies.pdf: chapter01/NetworkTopologies.svg

%-watch: main/%.tex
	mkdir -p $(BUILD_DIR)
	cd $(BUILD_DIR) ; $(LATEXMK_PVC) ../$<
