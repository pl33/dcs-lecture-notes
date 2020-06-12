
BUILD_DIR = build

LATEXMK = latexmk -pdf -silent -synctex=1
LATEXMK_PVC = $(LATEXMK) -pvc

ALL_CHAPTERS = $(BUILD_DIR)/chapter00.pdf $(BUILD_DIR)/chapter01.pdf $(BUILD_DIR)/chapter02.pdf $(BUILD_DIR)/chapter03.pdf $(BUILD_DIR)/chapter04.pdf $(BUILD_DIR)/chapter05.pdf $(BUILD_DIR)/chapter06.pdf
ALL_EXERCISES = $(BUILD_DIR)/exercise00.pdf $(BUILD_DIR)/exercise01.pdf $(BUILD_DIR)/exercise02.pdf $(BUILD_DIR)/exercise03.pdf $(BUILD_DIR)/exercise04.pdf $(BUILD_DIR)/exercise05.pdf $(BUILD_DIR)/exercise06.pdf
ALL_SVGS = $(BUILD_DIR)/svg/cc-by-4-0.pdf $(BUILD_DIR)/svg/ch01_EM_Spectrum_Properties.pdf $(BUILD_DIR)/svg/ch01_Electromagnetic-Spectrum.pdf $(BUILD_DIR)/svg/ch01_NetworkTopologies.pdf $(BUILD_DIR)/svg/ch03_Conv_Corr_Auto.pdf $(BUILD_DIR)/svg/ch04_win_blackman.pdf $(BUILD_DIR)/svg/ch04_win_hamming.pdf $(BUILD_DIR)/svg/ch04_win_hann.pdf $(BUILD_DIR)/svg/ch04_win_rect.pdf $(BUILD_DIR)/svg/ch04_win_tri.pdf $(BUILD_DIR)/svg/ch04_win_gauss.pdf $(BUILD_DIR)/svg/ch06_FFT_Butterfly.pdf
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
	inkscape -D -o $@ $<

$(BUILD_DIR)/svg_latex/%.pdf:
	mkdir -p $(BUILD_DIR)/svg_latex
	inkscape -D --export-latex -o $@ $<

$(BUILD_DIR)/svg/cc-by-4-0.pdf: common/cc-by-sa-4.0.svg
$(BUILD_DIR)/svg/ch01_EM_Spectrum_Properties.pdf: chapter01/EM_Spectrum_Properties_edit.svg
$(BUILD_DIR)/svg/ch01_Electromagnetic-Spectrum.pdf: chapter01/Electromagnetic-Spectrum.svg
$(BUILD_DIR)/svg/ch01_NetworkTopologies.pdf: chapter01/NetworkTopologies.svg
$(BUILD_DIR)/svg/ch03_Conv_Corr_Auto.pdf: chapter03/Comparison_convolution_correlation.svg
$(BUILD_DIR)/svg/ch04_win_blackman.pdf: chapter04/win_blackman.svg
$(BUILD_DIR)/svg/ch04_win_hamming.pdf: chapter04/win_hamming.svg
$(BUILD_DIR)/svg/ch04_win_hann.pdf: chapter04/win_hann.svg
$(BUILD_DIR)/svg/ch04_win_rect.pdf: chapter04/win_rect.svg
$(BUILD_DIR)/svg/ch04_win_tri.pdf: chapter04/win_tri.svg
$(BUILD_DIR)/svg/ch04_win_gauss.pdf: chapter04/win_gauss.svg
$(BUILD_DIR)/svg/ch06_FFT_Butterfly.pdf: chapter06/FFT_Butterfly.svg

%-watch: main/%.tex
	mkdir -p $(BUILD_DIR)
	cd $(BUILD_DIR) ; $(LATEXMK_PVC) ../$<
