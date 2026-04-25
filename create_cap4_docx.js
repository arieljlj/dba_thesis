const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
        AlignmentType, HeadingLevel, WidthType, BorderStyle, ShadingType, VerticalAlign } = require('docx');
const fs = require('fs');

// UIIX format standards:
// Font: Times New Roman 12pt
// Line spacing: 1.5
// Margins: Left 4cm, Right 2.5cm, Top 2.5cm, Bottom 2.5cm
// In DXA: 1cm ≈ 567 DXA
const margins = {
  left: 2268,    // 4 cm
  right: 1418,   // 2.5 cm
  top: 1418,     // 2.5 cm
  bottom: 1418   // 2.5 cm
};

const contentWidth = 12240 - margins.left - margins.right; // US Letter width - margins

const doc = new Document({
  styles: {
    default: {
      document: {
        run: { font: "Times New Roman", size: 24 }, // 12pt
        paragraph: { spacing: { line: 360, lineRule: "auto" } } // 1.5 spacing = 360 DXA
      }
    },
    paragraphStyles: [
      {
        id: "Heading1",
        name: "Heading 1",
        basedOn: "Normal",
        next: "Normal",
        run: { font: "Times New Roman", size: 24, bold: true }, // 12pt bold
        paragraph: {
          spacing: { line: 360, lineRule: "auto", before: 240, after: 240 },
          outlineLevel: 0
        }
      },
      {
        id: "Heading2",
        name: "Heading 2",
        basedOn: "Normal",
        next: "Normal",
        run: { font: "Times New Roman", size: 24, bold: true }, // 12pt bold
        paragraph: {
          spacing: { line: 360, lineRule: "auto", before: 200, after: 200 },
          outlineLevel: 1
        }
      },
      {
        id: "Heading3",
        name: "Heading 3",
        basedOn: "Normal",
        next: "Normal",
        run: { font: "Times New Roman", size: 24, bold: true }, // 12pt bold
        paragraph: {
          spacing: { line: 360, lineRule: "auto", before: 180, after: 180 },
          outlineLevel: 2
        }
      }
    ]
  },
  sections: [{
    properties: {
      page: {
        margin: margins
      }
    },
    children: [
      // Title
      new Paragraph({
        heading: HeadingLevel.HEADING_1,
        children: [new TextRun("Capítulo IV — Propuesta de Transformación")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({ text: "", spacing: { line: 360, lineRule: "auto" } }),

      // 4.1 Fundamentación
      new Paragraph({
        heading: HeadingLevel.HEADING_2,
        children: [new TextRun("4.1. Fundamentación de la Propuesta de Transformación")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("Hay una brecha de 48 puntos entre la intención emprendedora y la acción real. El Capítulo 3 mostró que el 68% de estudiantes dice que quiere emprender. Pero cuando se pregunta a actores del ecosistema cuántos egresados realmente crean empresas, la respuesta es el 20%. No es un problema de medición. Es una diferencia consistente que los datos confirman.")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("¿Por qué ocurre esto? El análisis de regresión mostró que la actitud hacia el emprendimiento predice aproximadamente el 48% de la intención emprendedora (R² = 0.478). Eso es importante. Pero no explica qué pasa después de que los estudiantes se gradúan. El problema está en que las actitudes positivas dependen del contexto. En la universidad, donde todos hablan de formalización y acceso a capital, los estudiantes desarrollan optimismo. Luego se gradúan y chocan con la realidad: no hay oportunidades claras, la informalidad es generalizada, y no conocen a nadie en el mundo empresarial legítimo. La actitud simplemente no sobrevive ese choque.")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("El conocimiento del ecosistema emprendedor agregó predicción significativa a la intención (β = 0.159, p < 0.001). Suena bien en números. Pero el análisis cualitativo muestra el problema real: ese conocimiento es general, no local. Los estudiantes entienden marcos conceptuales sobre emprendimiento y financiamiento. Lo que necesitan es información sobre qué funciona en su municipio específico, quiénes son los actores con poder de decisión, y cómo obtener legitimidad en redes locales. La información centralizada no produce agencia local.")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("Un hallazgo que llama la atención fue el efecto moderador del contexto universitario (β = 0.089, p = 0.031). La universidad amplifica la relación entre actitud e intención emprendedora. Eso tiene lógica: un ambiente que valora el emprendimiento refuerza las actitudes positivas. Pero los datos cualitativos revelan la limitación: amplificar la motivación no es suficiente. Los estudiantes necesitan recursos que la universidad sola no proporciona: mentoría continuada más allá del semestre, acceso a personas con experiencia real, legitimidad social en redes de negocios, y apoyo cuando fracasan.")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("Aquí viene lo interesante. Cuando se compararon las variables educativas, la mentoría académica (β = 0.118) superó significativamente el impacto de la alfabetización financiera (β = 0.067). Esto desafía la política pública colombiana que ha puesto todo el énfasis en acceso a crédito como la solución. La evidencia sugiere algo diferente: el acompañamiento humano, las conversaciones con personas que han estado en el mismo lugar, y la construcción de confianza a través de relaciones personales funcionan mejor que cursos sobre productos financieros.")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("El análisis cualitativo confirmó esto. Los estudiantes que fracasan en emprendimiento reportan desmoralización severa. Pero cuando ese fracaso ocurre con un mentor presente, la probabilidad de intentar de nuevo aumenta. Las barreras estructurales de acceso a redes y legitimidad son especialmente duras para emprendedores de necesidad, quienes enfrentan discriminación sistemática de instituciones que priorizan emprendedores con credenciales formales.")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("Todo esto justifica una intervención en tres niveles. Primero, política pública nacional diferenciada según tipo de emprendimiento. Segundo, instituciones universitarias que funcionan como intermediarias locales reales. Tercero, acompañamiento directo a estudiantes que facilita la transición de la intención a la acción. La propuesta que sigue es una respuesta específica a estas necesidades.")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({ text: "", spacing: { line: 360, lineRule: "auto" } }),

      // 4.2 Descripción
      new Paragraph({
        heading: HeadingLevel.HEADING_2,
        children: [new TextRun("4.2. Descripción de la Propuesta de Transformación")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("Se propone un Modelo de Fortalecimiento de la Intención Emprendedora mediante Intermediación Local y Mentoría Estructurada. El modelo parte de una idea simple: la transición de intención a acción no ocurre por convencimiento, sino por mediación. Alguien necesita conectar al estudiante con oportunidades reales, darle acceso a personas que han hecho lo que él intenta hacer, y estar ahí cuando todo falla.")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("El modelo opera simultáneamente en tres niveles. En el nivel nacional, propone bifurcar los programas de apoyo al emprendimiento: una rama para emprendedores que buscan crear negocios escalables con tecnología (oportunidad), y otra rama para personas que necesitan generar ingresos (necesidad). Esto responde a un hallazgo claro: políticas genéricas excluyen sistemáticamente a emprendedores de necesidad, que son la mayoría en universidades técnicas.")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("En el nivel universitario, se crea una estructura institucional que funciona como puente entre estudiantes e ecosistema local. Esta estructura incluye un programa de mentoría con mentores reales (docentes, empresarios locales, graduados exitosos), redes de estudiantes donde comparten problemas y soluciones, acceso formalizado a cámaras de comercio e incubadoras locales, y algo que la política ha ignorado: mecanismos específicos para recuperarse del fracaso. Que exista apoyo post-fracaso es importante porque el fracaso es norma en emprendimiento, no excepción.")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("En el nivel individual, el modelo actúa a través de tres mecanismos concretos. Primero, información local sobre viabilidad: un mentor que conoce el mercado local puede decir \"sí, eso funciona aquí\" o \"aquí no, pero prueba esto otro\". Eso es diferente a un curso general sobre emprendimiento. Segundo, fortalecimiento de confianza en sí mismo a través de conversaciones con alguien que ha enfrentado problemas similares. Tercero, acceso a referentes que demuestran que el emprendimiento es posible para personas como ellos.")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("Los cuatro principios que guían el modelo son claros. Mentalidad local: las soluciones no vienen de oficinas centrales, sino de entender qué funciona en cada territorio. Mentoría antes que dinero: el capital importa, pero la relación humana es lo que hace la diferencia. Legitimidad y redes antes que certificados: en el mercado local, quién te presenta importa más que qué papers tengas. Apoyo después del fracaso: si alguien fracasa y no hay red para sostenarlo, simplemente desiste.")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({ text: "", spacing: { line: 360, lineRule: "auto" } }),

      // 4.3 Objetivos
      new Paragraph({
        heading: HeadingLevel.HEADING_2,
        children: [new TextRun("4.3. Objetivos de la Propuesta")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        heading: HeadingLevel.HEADING_3,
        children: [new TextRun("Objetivo General.")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("Diseñar e implementar un modelo de intermediación local y mentoría que permita que más estudiantes universitarios colombianos pasen de la intención emprendedora a acciones concretas. La meta específica es reducir la brecha intención-acción de 48 puntos (68% intención vs. 20% acción) a un máximo de 30 puntos en el horizonte de 24 meses después de que los estudiantes se gradúan.")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        heading: HeadingLevel.HEADING_3,
        children: [new TextRun("Objetivos Específicos.")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("El primero es diseñar una estructura de mentoría con reglas claras: quiénes pueden ser mentores, cómo se preparan, cuánto tiempo duran las relaciones de mentoría, y cómo se verifica que funciona. Incluye también crear conexiones formales entre la institución y actores locales (cámaras, incubadoras, entidades de crédito).")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("El segundo es proponer que las políticas públicas nacionales reconozcan que emprendedores de oportunidad y de necesidad son diferentes y requieren apoyos diferentes. Una persona que quiere crear una startup tecnológica tiene necesidades distintas a alguien que intenta generar su propio ingreso por falta de empleo.")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("El tercero es especificar qué hace una institución cuando un estudiante ha intentado emprender y fracasó. ¿Cómo se le ayuda a procesar lo que aprendió? ¿Cómo se le anima a reintentar? ¿Hay fondos para un segundo intento?")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("El cuarto es establecer indicadores claros que permitan saber si el modelo funciona: ¿qué porcentaje de estudiantes que participan en mentoría pasan a acciones reales? ¿Mantienen las empresas después de dos años? ¿Sienten que pueden enfrentar nuevos desafíos?")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({ text: "", spacing: { line: 360, lineRule: "auto" } }),

      // 4.4 Actividades y Fases
      new Paragraph({
        heading: HeadingLevel.HEADING_2,
        children: [new TextRun("4.4. Actividades, Fases y/o Etapas")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("El modelo se ejecuta en tres fases que responden a momentos críticos en la vida del estudiante. Cada fase tiene actividades específicas.")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        heading: HeadingLevel.HEADING_3,
        children: [new TextRun("Fase 1: Diagnóstico y Diseño (Semestres 1 y 2).")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("Antes de lanzar nada, la institución necesita saber qué tiene disponible. Una auditoría responde preguntas simples: ¿hay docentes con experiencia empresarial? ¿Qué relaciones ya existen con cámaras de comercio o incubadoras? ¿Qué tan sólida es la base de datos de egresados? Esta auditoría produce un panorama claro de fortalezas que se pueden usar y vacíos que hay que llenar.")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("Luego vienen sesiones de diseño participativo. Se invitan estudiantes con intención emprendedora, profesores, actores del ecosistema local, y directivos de la institución. Juntos definen: ¿cómo es un buen mentor para nuestro contexto? ¿Qué obstáculos enfrentan los emprendedores locales? ¿Qué instituciones tienen poder real para abrir puertas? El resultado es un modelo adaptado a la realidad específica, no un copiar-pegar de otro lado.")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        heading: HeadingLevel.HEADING_3,
        children: [new TextRun("Fase 2: Construcción de Infraestructura (Semestres 3 y 4).")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("Ahora se construye lo que funcionará. La formalización de mentoría incluye: seleccionar mentores con criterios claros (no solo que sean empresarios, sino que sepan acompañar); capacitarlos en mentoría y en comprensión de dinámicas emocionales; definir que cada relación dura al menos seis meses; establecer seguimiento de calidad. No se deja a la suerte.")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("Las alianzas con actores locales se concretan en acuerdos escritos. La cámara de comercio ofrece X. La incubadora local ofrece Y. MinCIT proporciona información sobre crédito. Las cajas de compensación ofrecen servicios técnicos. Cada compromiso está documentado.")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("Se crean redes de salvaguarda para después del fracaso: un grupo de asesoría especializado, acceso a nuevas cohortes de mentoría para reintentos, y un pequeño fondo rotatorio que permite pequeñas inversiones para un segundo intento. Esto es lo que diferencia este modelo de otros.")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        heading: HeadingLevel.HEADING_3,
        children: [new TextRun("Fase 3: Operación y Evaluación (Semestre 5 en adelante).")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("El modelo entra en funcionamiento. Se identifican estudiantes con intención emprendedora significativa, se emparejan con mentores, se coordina el proceso. Luego comienza el seguimiento: a los 6 meses post-egreso, se contacta a los estudiantes para preguntar si iniciaron algo. A los 12 meses, si mantienen lo iniciado. A los 24 meses, se hace una evaluación completa.")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({ text: "", spacing: { line: 360, lineRule: "auto" } }),

      // 4.5 Recursos
      new Paragraph({
        heading: HeadingLevel.HEADING_2,
        children: [new TextRun("4.5. Recursos Necesarios")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("Cuatro dimensiones de recursos: humanos, financieros, tecnológicos, institucionales.")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("En recursos humanos, se necesita un coordinador de tiempo completo (que gestione día a día), mentores empresariales (para una cohorte inicial de 50 estudiantes, entre 10 y 15 mentores), y apoyo administrativo (0.5 FTE). Los mentores pueden venir de dentro de la institución, del mundo empresarial local, o de graduados exitosos.")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("En presupuesto, se estima entre 30 y 50 millones de pesos anuales (en valores 2026). Esto incluye: salarios del coordinador y staff (40-50%), honorarios para mentores que no son docentes (5-10%), gastos operativos (10-15%), y seguimiento longitudinal (15-25%). Es viable combinando presupuesto institucional con alianzas público-privadas.")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("En tecnología, se necesita una plataforma que registre mentores y estudiantes, documente reuniones, recopile retroalimentación, y aplique instrumentos de medición. Puede ser un CRM configurado para educación, un LMS, o un sistema personalizado con software libre. También acceso a herramientas de videollamadas para mentoría a distancia.")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("En recursos institucionales, lo más importante es compromiso real de la rectoría (no solo declaraciones). Los docentes necesitan tiempo dentro de su carga para mentoría. El modelo debe estar integrado con cursos de emprendimiento y proyectos de carrera. Las alianzas externas deben formalizarse por escrito.")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({ text: "", spacing: { line: 360, lineRule: "auto" } }),

      // 4.6 Resultados
      new Paragraph({
        heading: HeadingLevel.HEADING_2,
        children: [new TextRun("4.6. Resultados")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        heading: HeadingLevel.HEADING_3,
        children: [new TextRun("4.6.1. Resultados o Productos a Obtener")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("El modelo produce resultados tangibles. El primero es un Protocolo de Mentoría Empresarial que codifica los procedimientos: cómo seleccionar mentores, estructura de un plan de mentoría, cómo manejar fracasos, cómo evaluar calidad. Este protocolo es el documento operativo que una institución usa diariamente.")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("El segundo es un Manual de Intermediación Local para universidades técnicas que sistematiza el aprendizaje: marco conceptual, pasos del diagnóstico, metodologías participativas, plantillas para alianzas, estándares de mentoría, instrumentos de seguimiento, casos de éxito. Es un bien público que otras instituciones pueden adaptar.")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("El tercero es la constitución de una cohorte piloto de al menos 50 estudiantes en mentoría activa. Esta cohorte recibe seguimiento riguroso y genera los datos iniciales sobre viabilidad.")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("El cuarto es un Informe de Resultados que documenta hallazgos a 12 meses post-egreso: tasas de transición intención-acción, factores de éxito o fracaso, historias de impacto, aprendizajes sobre ajustes necesarios al protocolo.")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        heading: HeadingLevel.HEADING_3,
        children: [new TextRun("4.6.2. Indicadores, Criterios de Evaluación y de Instrumentación")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("La evaluación tiene tres niveles. Los indicadores de proceso miden si las actividades se ejecutan como se planeó. El indicador principal es: ¿qué porcentaje de estudiantes identificados con intención logran acceso a mentoría? Meta: 70% en el primer año. Esto requiere registro sistemático de quiénes tienen intención, quiénes son invitados, quiénes aceptan, quiénes son emparejados.")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("Los indicadores de resultado miden cambios en comportamiento. El más importante es la tasa de transición intención-acción dentro de 6 meses post-egreso (definida como registro formal de empresa). Meta: 30-40%, versus el 20% observado sin mentoría. Esto es un incremento de 50-100% en la tasa. Se mide mediante seguimiento longitudinal directo.")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("A 24 meses post-egreso, se pregunta: ¿qué porcentaje de quienes iniciaron empresa mantiene operaciones activas? Meta: 60%. Esto refleja la calidad del acompañamiento post-inicio.")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("El indicador de moderación central es la diferencia en tasas de transición entre grupo con mentoría y grupo de comparación sin ella. Idealmente, esto se mide con un diseño randomizado que permite atribuir causalmente el cambio a la intervención.")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("Indicadores cualitativos incluyen narrativas de estudiantes sobre cambios en confianza en sí mismos, acceso a redes, y aceptación social de la identidad emprendedora. Se recopilan mediante entrevistas.")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({ text: "", spacing: { line: 360, lineRule: "auto" } }),

      // 4.7 Valoración
      new Paragraph({
        heading: HeadingLevel.HEADING_2,
        children: [new TextRun("4.7. Valoración, Evaluación y Validación de la Propuesta")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("¿Es viable? Sí, con condiciones. Técnicamente es implementable en universidades técnicas colombianas si hay compromiso real de la rectoría, actores locales dispuestos a colaborar, y sistemas de información mínimamente funcionales. Financieramente es sostenible: 30-50 millones anuales es un presupuesto manejable para universidades de tamaño medio, y hay múltiples fuentes posibles (presupuesto institucional, MinCIT, fondos de cooperación internacional, responsabilidad social empresarial).")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("Políticamente se alinea parcialmente con prioridades nacionales. MinCIT enfatiza formalización y acceso a crédito. La Ley 2069 menciona explícitamente mentoría y capacitación. Pero aún no hay reconocimiento claro de que emprendedores de oportunidad y de necesidad son grupos diferentes. Eso es una debilidad del entorno político que el modelo puede ayudar a cambiar si demuestra efectividad.")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("¿Cuáles son las fortalezas? Está fundamentada en evidencia rigurosa de la investigación, no en suposiciones. Cada componente (mentoría, contexto local, apoyo post-fracaso) emerge directo de los datos del Capítulo 3. Está localizada, no centralizada. Enfatiza mecanismos que funcionan (mentoría continuada) más que lo que la política ha priorizado sin evidencia (capital inicial).")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("¿Cuáles son las limitaciones? La efectividad depende de la calidad de los mentores, que es difícil de asegurar sistemáticamente. El modelo alcanza solo educación superior acreditada, no cubre SENA ni educación media. No resuelve barreras macroeconómicas: desempleo persistente, informalidad sistemática, volatilidad de mercados. Una mentoría excelente no crea oportunidades donde la estructura económica no las genera. Y parte de la transición intención-acción depende de factores fuera del control de la institución: acceso a crédito, ciclos económicos, cambios en regulación.")],
        spacing: { line: 360, lineRule: "auto" }
      }),
      new Paragraph({
        children: [new TextRun("Los próximos pasos para validación son cuatro. Primero, validación con actores relevantes (estudiantes, docentes, empresarios, autoridades) antes de implementación completa. Segundo, ejecución de un piloto en COTECNOVA u otra institución técnica con registro riguroso. Tercero, evaluación mediante diseño robusto, preferiblemente un ensayo randomizado controlado que permita atribuir causalmente el cambio. Cuarto, difusión de resultados mediante publicaciones académicas, manuales para otras instituciones, y participación en espacios de política pública para informar cambios en programas nacionales.")],
        spacing: { line: 360, lineRule: "auto" }
      })
    ]
  }]
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync("docs/05_cap4_propuesta_transformacion/Capitulo_4_Propuesta_Transformacion.docx", buffer);
  console.log("Documento creado exitosamente.");
});
