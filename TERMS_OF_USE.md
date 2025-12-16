# DataSearcher - TERMS OF USE & CRITICAL LICENSE AGREEMENT

## 1. Acceptance of Terms

By using the DataSearcher software (the "Software"), you agree to be bound by these Terms of Use and all applicable laws and regulations. If you do not agree with any of these terms, you are prohibited from using or accessing the Software.

## 2. General Usage License

The Software is provided "as is" for general purpose scanning and file analysis. The Software is licensed, not sold. You are granted a non-exclusive, non-transferable, revocable license to use the Software strictly in accordance with these terms.

## 3. Mandatory Maintenance & Modification Restrictions

The internal architecture of the Software is highly optimized, fragmented, and relies on strict dependencies. Any modification to the core structure voids this license and is strictly prohibited.

### ⚠️ A. Core System Integrity Violations (MAJOR RISK)

The following modifications will permanently disable the Software and result in immediate license termination:

* **Function and Variable Renaming:** You MUST NOT change single-letter function names (e.g., `d`, `c`, `a`, `s`, `m`) or internal variable names within the core utility scripts (located in the `data/` folder). These names are hardcoded across multiple modules for internal communication.
* **Directory Structure Alteration:** You MUST NOT rename, move, or delete any folders within the `data/utilities/` structure (e.g., `scanner/`, `interface/`). The software relies on these fixed relative paths to function and to manage updates.
* **The 'VERSION' File:** This file MUST NOT be deleted or manually edited outside of the official update process. It is vital for the update checking logic (`c.py`).

### 📡 B. Remote Update System (R.U.S.) Restrictions

The Software includes an integrated Remote Update System (R.U.S.) to ensure security and functionality. Tampering with the R.U.S. is strictly forbidden:

* **GitHub API URL:** You MUST NOT modify the GitHub API URL (`J` variable in `data/c.py`). This URL is the sole hardcoded endpoint for verifying official Software releases.
* **Asset Naming:** When distributing or modifying local files, you MUST ensure that file names (e.g., `m.py`, `i.py`) remain unchanged, as the R.U.S. dynamically searches for these exact names during an update.

---
🇫🇷 CONDITIONS D'UTILISATION ET ACCORD DE LICENCE CRITIQUE

## 1. Acceptation des Conditions

En utilisant le logiciel DataSearcher (le « Logiciel »), vous acceptez d'être lié par les présentes Conditions d'Utilisation et toutes les lois et réglementations applicables. Si vous n'acceptez pas ces conditions, l'accès ou l'utilisation du Logiciel vous est interdit.

## 3. Restrictions Obligatoires de Maintenance et de Modification

L'architecture interne du Logiciel est hautement optimisée, fragmentée et repose sur des dépendances strictes. Toute modification de la structure de base annule cette licence et est strictement interdite.

### ⚠️ A. Violations de l'Intégrité du Système Central (RISQUE MAJEUR)

Les modifications suivantes désactiveront définitivement le Logiciel et entraîneront la résiliation immédiate de la licence :

* **Renommage des Fonctions et Variables :** Vous NE DEVEZ PAS changer les noms de fonctions à une seule lettre (par exemple, `d`, `c`, `a`, `s`, `m`) ni les noms de variables internes dans les scripts utilitaires (situés dans le dossier `data/`). Ces noms sont codés en dur dans plusieurs modules pour la communication interne.
* **Altération de la Structure des Répertoires :** Vous NE DEVEZ PAS renommer, déplacer ou supprimer les dossiers dans la structure `data/utilities/` (par exemple, `scanner/`, `interface/`). Le logiciel dépend de ces chemins relatifs fixes pour fonctionner et gérer les mises à jour.
* **Le Fichier 'VERSION' :** Ce fichier NE DOIT PAS être supprimé ou édité manuellement en dehors du processus de mise à jour officiel. Il est vital pour la logique de vérification de mise à jour (`c.py`).

### 📡 B. Restrictions du Système de Mise à Jour à Distance (R.U.S.)

Le Logiciel comprend un Système de Mise à Jour à Distance (R.U.S.) intégré pour assurer la sécurité. Toute manipulation du R.U.S. est strictement interdite :

* **URL de l'API GitHub :** Vous NE DEVEZ PAS modifier l'URL de l'API GitHub (variable `J` dans `data/c.py`). Cette URL est le seul point d'accès codé en dur pour vérifier les publications officielles du Logiciel.
* **Nommage des Assets :** Lors de la distribution ou de la modification de fichiers locaux, vous DEVEZ vous assurer que les noms de fichiers (par exemple, `m.py`, `i.py`) restent inchangés, car le R.U.S. recherche dynamiquement ces noms exacts lors d'une mise à jour.

---
🇪🇸 TÉRMINOS DE USO Y ACUERDO DE LICENCIA CRÍTICO

## 1. Aceptación de los Términos

Al utilizar el software DataSearcher (el "Software"), usted acepta regirse por estos Términos de Uso y todas las leyes y regulaciones aplicables. Si no está de acuerdo con alguno de estos términos, se le prohíbe usar o acceder al Software.

## 3. Restricciones Obligatorias de Mantenimiento y Modificación

La arquitectura interna del Software está altamente optimizada, fragmentada y se basa en dependencias estrictas. Cualquier modificación a la estructura central anula esta licencia y está estrictamente prohibida.

### ⚠️ A. Violaciones de la Integridad del Sistema Central (RIESGO MAYOR)

Las siguientes modificaciones deshabilitarán permanentemente el Software y resultarán en la terminación inmediata de la licencia:

* **Cambio de Nombre de Funciones y Variables:** NO DEBE cambiar los nombres de funciones de una sola letra (p. ej., `d`, `c`, `a`, `s`, `m`) ni los nombres de variables internas en los scripts de utilidad centrales (ubicados en la carpeta `data/`). Estos nombres están codificados para la comunicación interna.
* **Alteración de la Estructura de Directorios:** NO DEBE renombrar, mover o eliminar ninguna carpeta dentro de la estructura `data/utilities/` (p. ej., `scanner/`, `interface/`). El software depende de estas rutas relativas fijas para funcionar y gestionar las actualizaciones.
* **El Archivo 'VERSION':** Este archivo NO DEBE eliminarse ni editarse manualmente fuera del proceso de actualización oficial. Es vital para la lógica de verificación de actualizaciones (`c.py`).

### 📡 B. Restricciones del Sistema de Actualización Remota (R.U.S.)

El Software incluye un Sistema de Actualización Remota (R.U.S.) integrado para garantizar la seguridad. Está estrictamente prohibido manipular el R.U.S.:

* **URL de la API de GitHub:** NO DEBE modificar la URL de la API de GitHub (variable `J` en `data/c.py`). Esta URL es el único punto final codificado para verificar los lanzamientos oficiales del Software.
* **Nomenclatura de Assets:** Al distribuir o modificar archivos locales, DEBE asegurarse de que los nombres de los archivos (p. ej., `m.py`, `i.py`) permanezcan sin cambios, ya que el R.U.S. busca dinámicamente estos nombres exactos durante una actualización.
