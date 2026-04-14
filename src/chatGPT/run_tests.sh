#!/bin/bash
# run_tests.sh - Script mejorado con soporte para entornos virtuales

echo "════════════════════════════════════════════════════════════════════════"
echo "🧪 EJECUTANDO SUITE DE PRUEBAS UNITARIAS PARA CALCULADORA RPN"
echo "════════════════════════════════════════════════════════════════════════"

# Colores para output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m'

# Función para verificar si estamos en un entorno virtual
in_virtualenv() {
    if [ -n "$VIRTUAL_ENV" ]; then
        return 0  # Está en venv
    else
        return 1  # No está en venv
    fi
}

# Función para crear y activar entorno virtual
setup_venv() {
    echo -e "${BLUE}📦 Configurando entorno virtual Python...${NC}"
    
    if [ ! -d "venv" ]; then
        echo "   Creando venv..."
        python3 -m venv venv
    else
        echo "   Entorno virtual existente encontrado."
    fi
    
    echo "   Activando venv..."
    source venv/bin/activate
    
    echo "   Instalando dependencias..."
    pip install --upgrade pip > /dev/null 2>&1
    pip install -r requirements.txt
}

# Verificar si pytest está disponible
if ! python -c "import pytest" 2>/dev/null; then
    echo -e "${YELLOW}⚠️  pytest no encontrado.${NC}"
    
    if ! in_virtualenv; then
        echo -e "${YELLOW}   No estás en un entorno virtual.${NC}"
        echo ""
        echo -e "${BLUE}📋 Opciones disponibles:${NC}"
        echo "   1. Crear entorno virtual automáticamente (recomendado)"
        echo "   2. Usar pipx (si está instalado)"
        echo "   3. Instalar paquetes del sistema (apt)"
        echo "   4. Abortar"
        echo ""
        read -p "   Elige una opción [1-4]: " choice
        
        case $choice in
            1)
                setup_venv
                ;;
            2)
                echo -e "${BLUE}   Verificando pipx...${NC}"
                if ! command -v pipx &> /dev/null; then
                    echo -e "${RED}   pipx no está instalado.${NC}"
                    echo "   Instálalo con: sudo apt install pipx"
                    exit 1
                fi
                echo "   Instalando pytest con pipx..."
                pipx install pytest
                pipx install pytest-cov
                pipx ensurepath
                echo -e "${YELLOW}   ⚠️  Reinicia tu terminal o ejecuta: source ~/.bashrc${NC}"
                exit 0
                ;;
            3)
                echo -e "${BLUE}   Instalando python3-pytest desde apt...${NC}"
                sudo apt update
                sudo apt install -y python3-pytest python3-pytest-cov
                ;;
            4)
                echo "   Abortando."
                exit 1
                ;;
            *)
                echo -e "${RED}   Opción inválida. Abortando.${NC}"
                exit 1
                ;;
        esac
    else
        echo -e "${YELLOW}   Instalando dependencias en el entorno virtual actual...${NC}"
        pip install -r requirements.txt
    fi
fi

echo ""
echo "📊 Ejecutando pruebas con cobertura..."
echo "────────────────────────────────────────────────────────────────────────"

# Verificar si el módulo rpn.py existe
if [ ! -f "rpn.py" ]; then
    echo -e "${RED}❌ Error: No se encuentra rpn.py en el directorio actual.${NC}"
    exit 1
fi

# Ejecutar pytest con cobertura
if pytest test_rpn.py \
    --cov=rpn \
    --cov-report=term-missing \
    --cov-report=html \
    --cov-report=xml \
    --cov-fail-under=90 \
    -v; then
    
    TEST_RESULT=$?
    
    echo ""
    echo -e "${GREEN}════════════════════════════════════════════════════════════════════════${NC}"
    echo -e "${GREEN}✅ TODAS LAS PRUEBAS PASARON - COBERTURA >= 90%${NC}"
    echo -e "${GREEN}════════════════════════════════════════════════════════════════════════${NC}"
    echo ""
    echo "📁 Reportes generados:"
    echo "   • HTML: $(pwd)/htmlcov/index.html"
    echo "   • XML:  $(pwd)/coverage.xml"
    echo ""
    
    # Preguntar si abrir reporte HTML
    if command -v xdg-open &> /dev/null || command -v open &> /dev/null; then
        read -p "   ¿Abrir reporte HTML en navegador? [s/N]: " open_choice
        if [[ "$open_choice" =~ ^[Ss]$ ]]; then
            if command -v open &> /dev/null; then
                open htmlcov/index.html
            else
                xdg-open htmlcov/index.html
            fi
        fi
    fi
    
else
    TEST_RESULT=$?
    echo ""
    echo -e "${RED}════════════════════════════════════════════════════════════════════════${NC}"
    
    if [ $TEST_RESULT -eq 5 ]; then
        echo -e "${RED}❌ PRUEBAS PASARON PERO COBERTURA < 90%${NC}"
    else
        echo -e "${RED}❌ PRUEBAS FALLIDAS${NC}"
    fi
    
    echo -e "${RED}════════════════════════════════════════════════════════════════════════${NC}"
    exit 1
fi

# Sugerir desactivar venv si está activo
if in_virtualenv; then
    echo ""
    echo -e "${BLUE}💡 Recuerda: Estás en un entorno virtual. Para salir ejecuta: deactivate${NC}"
fi