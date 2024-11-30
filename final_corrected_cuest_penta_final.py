import streamlit as st

# Preguntas, respuestas y justificaciones
questions = [{'question': "La traducción más exacta para la palabra 'Pentateuco' es:", 'options': ['Cinco Libros', 'La Ley', 'Cinco Rollos', 'La Torá'], 'answer': 'Cinco Rollos', 'justification': "El término 'Pentateuco' proviene del griego y se traduce como 'cinco rollos', refiriéndose a los cinco primeros libros de la Biblia.", 'type': 'multiple_choice'}, {'question': 'El cuarto documento del Pentateuco, conocido como Números, Arithmoi, tiene su mejor nombre en hebreo significando:', 'options': ['Comienzos', 'Estos son los nombres', 'En el desierto', 'Segunda Ley'], 'answer': 'En el desierto', 'justification': "El nombre hebreo de Números es 'Bemidbar', que significa 'en el desierto', describiendo el contexto geográfico principal del libro.", 'type': 'multiple_choice'}, {'question': '¿Qué campo abarca la narrativa de la creación en el Pentateuco?', 'options': ['Campo Ético', 'Campo Cósmico', 'Campo Histórico', 'Campo Profético'], 'answer': 'Campo Cósmico', 'justification': 'El relato de la creación en Génesis cubre el campo cósmico, abordando la creación del universo y todo lo que existe.', 'type': 'multiple_choice'}, {'question': 'Según los primeros 5 libros de la Biblia, el autor del Pentateuco es:', 'options': ['Moisés', 'Esdras', 'Sacerdotes', 'Anónimo'], 'answer': 'Anónimo', 'justification': 'Aunque la tradición atribuye el Pentateuco a Moisés, los textos no identifican específicamente un autor.', 'type': 'multiple_choice'}, {'question': 'El término Toráh tiene como significado:', 'options': ['Enseñanza', 'La Ley', 'Principio', 'Sumario teológico'], 'answer': 'Enseñanza', 'justification': "Toráh, en hebreo, significa 'enseñanza' o 'instrucción', y abarca leyes, narrativas y principios éticos.", 'type': 'multiple_choice'}, {'question': '¿En qué capítulo de Levítico se encuentra la descripción del holocausto y cuál es su propósito principal?', 'options': ['Capítulo 2; Propósito de acción de gracias', 'Capítulo 3; Propósito de purificación de impurezas rituales', 'Capítulo 1; Propósito de propiciación y consagración completa', 'Capítulo 4; Propósito de expiación por el pecado'], 'answer': 'Capítulo 1; Propósito de propiciación y consagración completa', 'justification': 'Levítico 1 describe el holocausto, cuyo propósito es la propiciación y consagración total a Dios mediante el sacrificio.', 'type': 'multiple_choice'}, {'question': "¿Cuál es el significado del término 'holocausto' en hebreo?", 'options': ['Ofrenda de paz', 'Sacrificio quemado', 'Ofrenda por el pecado', 'Ofrenda de comunión'], 'answer': 'Sacrificio quemado', 'justification': 'El término holocausto se refiere a un sacrificio que es quemado completamente en el altar como símbolo de entrega total.', 'type': 'multiple_choice'}, {'question': '¿Cuál es la característica distintiva de la ofrenda de paz en Levítico?', 'options': ['Se consume por completo en el altar', 'Se divide en tres partes: una para Dios, una para los sacerdotes y una para el oferente y su familia', 'Su propósito principal es la expiación por el pecado', 'Representa a Jesucristo como Redentor'], 'answer': 'Se divide en tres partes: una para Dios, una para los sacerdotes y una para el oferente y su familia', 'justification': 'La ofrenda de paz se comparte entre Dios, los sacerdotes y el oferente, simbolizando comunión y gratitud.', 'type': 'multiple_choice'}, {'question': '¿Cuál es el propósito principal de la ofrenda por el pecado en Levítico?', 'options': ['Expresar gratitud y comunión con Dios', 'Propiciar y purificar al oferente de sus pecados o transgresiones', 'Celebrar festividades religiosas', 'Compartir una comida en comunión con Dios y otros'], 'answer': 'Propiciar y purificar al oferente de sus pecados o transgresiones', 'justification': 'La ofrenda por el pecado se realiza para la purificación y reconciliación con Dios mediante el perdón de pecados.', 'type': 'multiple_choice'}, {'question': 'Con respecto a la estructura quiástica de Levítico, su tema central es:', 'options': ['Sacrificios Rituales', 'Sacerdotes consagrados', 'Pureza ritual', 'Día de la Expiación'], 'answer': 'Día de la Expiación', 'justification': 'El Día de la Expiación es central en Levítico, representando el momento en el que se realiza la reconciliación del pueblo con Dios.', 'type': 'multiple_choice'}, {'question': '¿Cuál es el tema principal de Levítico 1-7?', 'options': ['Las leyes de pureza', 'Las leyes sobre el diezmo', 'Las ofrendas y sacrificios', 'La consagración de los sacerdotes'], 'answer': 'Las ofrendas y sacrificios', 'justification': 'Levítico 1-7 detalla las diversas ofrendas y sacrificios, estableciendo normas para los diferentes tipos de adoración.', 'type': 'multiple_choice'}, {'question': "¿Qué significa el nombre hebreo de Levítico, 'Wayiqrá'?", 'options': ['Santidad', 'Él llamó', 'Sacrificio', 'Adoración'], 'answer': 'Él llamó', 'justification': "Wayiqrá significa 'Él llamó', reflejando el inicio del libro en el que Dios llama a Moisés desde el Tabernáculo.", 'type': 'multiple_choice'}, {'question': '¿Quién es el autor tradicionalmente reconocido de Levítico?', 'options': ['Aarón', 'Moisés', 'Josué', 'David'], 'answer': 'Moisés', 'justification': 'La autoría de Levítico se atribuye tradicionalmente a Moisés, quien recibió las leyes de Dios para Israel.', 'type': 'multiple_choice'}, {'question': '¿Cuál es el propósito teológico básico del libro de Levítico?', 'options': ['Enseñar la historia de los levitas', 'Establecer una comunidad consagrada al servicio del Señor', 'Explicar las leyes civiles', 'Detallar la genealogía de Israel'], 'answer': 'Establecer una comunidad consagrada al servicio del Señor', 'justification': 'Levítico se centra en santidad y pureza, estableciendo normas para consagrar al pueblo de Israel al servicio de Dios.', 'type': 'multiple_choice'}, {'question': "¿Qué tipo de ofrenda es descrita en Levítico 1 como 'holocausto'?", 'options': ['Ofrenda de paz', 'Ofrenda de cereal', 'Ofrenda quemada', 'Ofrenda por la culpa'], 'answer': 'Ofrenda quemada', 'justification': 'El holocausto es una ofrenda completamente quemada en el altar, representando dedicación total a Dios.', 'type': 'multiple_choice'}, {'question': '¿Qué simboliza el holocausto en el sistema sacrificial?', 'options': ['Gratitud a Dios', 'Expiación por el pecado y consagración total', 'Purificación ritual', 'Comunión con Dios'], 'answer': 'Expiación por el pecado y consagración total', 'justification': 'El holocausto simboliza la consagración total a Dios y el sacrificio necesario para la expiación de pecados.', 'type': 'multiple_choice'}, {'question': '¿Qué elemento NO está presente en la ofrenda de cereal?', 'options': ['Aceite', 'Harina', 'Sal', 'Levadura'], 'answer': 'Levadura', 'justification': 'La levadura está excluida de la ofrenda de cereal, que simboliza pureza y santidad.', 'type': 'multiple_choice'}, {'question': '¿Qué ofrenda se ofrecía en casos de comunión y agradecimiento?', 'options': ['Ofrenda por la culpa', 'Ofrenda de paz', 'Ofrenda de pecado', 'Ofrenda quemada'], 'answer': 'Ofrenda de paz', 'justification': 'La ofrenda de paz era ofrecida en reconocimiento de la comunión y gratitud hacia Dios.', 'type': 'multiple_choice'}, {'question': '¿Qué elemento adicional incluía la ofrenda por la culpa además del sacrificio animal?', 'options': ['Pan', 'Vino', 'Restitución a la persona afectada', 'Cereal'], 'answer': 'Restitución a la persona afectada', 'justification': 'La ofrenda por la culpa requería compensación económica o restitución a la persona afectada, además del sacrificio.', 'type': 'multiple_choice'}, {'question': '¿Cuál era la instrucción para el fuego en el altar del holocausto según Levítico 6:8-13?', 'options': ['Apagarlo después de cada sacrificio', 'Mantenerlo encendido día y noche', 'Encenderlo solo en días santos', 'Dejar que se apague en la noche'], 'answer': 'Mantenerlo encendido día y noche', 'justification': 'Dios ordenó que el fuego en el altar se mantuviera encendido constantemente, simbolizando el servicio continuo.', 'type': 'multiple_choice'}, {'question': '¿Qué ofrenda se hacía cuando alguien cometía un delito o transgresión específica?', 'options': ['Ofrenda por el pecado', 'Ofrenda de paz', 'Ofrenda por la culpa', 'Ofrenda de cereal'], 'answer': 'Ofrenda por la culpa', 'justification': 'La ofrenda por la culpa se ofrecía cuando alguien cometía un pecado que requería compensación o restitución.', 'type': 'multiple_choice'}, {'question': '¿Qué importancia tiene el sistema sacrificial de Levítico en la teología cristiana?', 'options': ['Solo tenía importancia histórica', 'Prefigura la obra redentora de Cristo', 'Solo aplicaba a los israelitas', 'Es irrelevante para el Nuevo Testamento'], 'answer': 'Prefigura la obra redentora de Cristo', 'justification': 'Los sacrificios del Antiguo Testamento prefiguran el sacrificio de Cristo, quien cumplió y perfeccionó el sistema sacrificial.', 'type': 'multiple_choice'}, {'question': '¿Cuál es el centro del quiasmo en la estructura del libro de Levítico?', 'options': ['El capítulo 16, que describe el Día de la Expiación.', 'El pasaje que trata sobre la santidad de Dios y la impureza del hombre.', 'El versículo que habla de la Ley como un signo eterno entre Dios y su pueblo.', 'Ninguna de las anteriores, ya que el centro del quiasmo en Levítico es un tema de debate entre los estudiosos.'], 'answer': 'El capítulo 16, que describe el Día de la Expiación.', 'justification': 'El quiasmo en Levítico tiene su punto central en el Día de la Expiación, que es clave para la teología de reconciliación con Dios.', 'type': 'multiple_choice'}, {'question': '¿Cuál era el significado simbólico de la sangre en los sacrificios?', 'options': ['Representaba la vida y era necesaria para la expiación del pecado.', 'Era un símbolo de poder y autoridad divina.', 'Solo tenía un significado ritual y no tenía un valor simbólico más profundo.', 'Representaba la unión entre el hombre y la naturaleza.'], 'answer': 'Representaba la vida y era necesaria para la expiación del pecado.', 'justification': 'La sangre simboliza la vida y es fundamental para el acto de expiación, como se enseña en Levítico.', 'type': 'multiple_choice'}, {'question': '¿Qué función principal tenían los sacerdotes según el texto?', 'options': ['Servir en el ejército.', 'Administrar propiedades.', 'Ser intercesores y representantes ante Dios.', 'Realizar trabajos manuales.'], 'answer': 'Ser intercesores y representantes ante Dios.', 'justification': 'Los sacerdotes eran intermediarios entre Dios y el pueblo, responsables de ofrecer sacrificios y de la purificación.', 'type': 'multiple_choice'}, {'question': '¿Qué representaban las piedras preciosas en el pectoral del sumo sacerdote?', 'options': ['Las tribus de Israel.', 'La riqueza del sacerdote.', 'La pureza del sumo sacerdote.', 'Los animales sacrificados.'], 'answer': 'Las tribus de Israel.', 'justification': 'Las doce piedras del pectoral representaban a las doce tribus de Israel, simbolizando la presencia de cada una ante Dios.', 'type': 'multiple_choice'}, {'question': '¿Qué evento confirmó la aceptación divina del servicio sacerdotal de Aarón y sus hijos?', 'options': ['La construcción del Tabernáculo.', 'La manifestación de la gloria de Dios.', 'La adoración al becerro de oro.', 'La llegada de Moisés al monte.'], 'answer': 'La manifestación de la gloria de Dios.', 'justification': 'La manifestación de la gloria de Dios en el Tabernáculo confirmó el llamado y el servicio de Aarón y sus hijos.', 'type': 'multiple_choice'}, {'question': '¿Por qué fueron castigados los hijos de Aarón, Nadab y Abiú?', 'options': ['Por no asistir a la ceremonia de consagración.', 'Por ofrecer un sacrificio incorrecto.', 'Por no vestirse adecuadamente.', 'Por no comer las partes de los animales sacrificados.'], 'answer': 'Por ofrecer un sacrificio incorrecto.', 'justification': "Nadab y Abiú fueron castigados por ofrecer 'fuego extraño' delante de Dios, desobedeciendo sus instrucciones.", 'type': 'multiple_choice'}, {'question': '¿Cuál era el propósito de las leyes sobre la impureza relacionada con las emisiones?', 'options': ['Evaluar la moralidad de las personas.', 'Mantener la pureza religiosa y biológica.', 'Prohibir las relaciones sexuales.', 'Controlar las enfermedades contagiosas.'], 'answer': 'Mantener la pureza religiosa y biológica.', 'justification': 'Estas leyes buscaban asegurar la pureza del pueblo en términos de prácticas y salud ritual.', 'type': 'multiple_choice'}, {'question': '¿Qué evento se conmemora en el Día de la Expiación?', 'options': ['La resurrección de Jesús.', 'La creación del mundo.', 'La liberación de los esclavos en Egipto.', 'La purificación y expiación de los pecados del pueblo de Israel.'], 'answer': 'La purificación y expiación de los pecados del pueblo de Israel.', 'justification': 'El Día de la Expiación es el día en que el sumo sacerdote realizaba sacrificios por los pecados del pueblo, buscando el perdón de Dios.', 'type': 'multiple_choice'}, {'question': '¿Qué hacía el sumo sacerdote en el Día de la Expiación?', 'options': ['Ofrecía sacrificios para sí mismo.', 'Realizaba un ayuno riguroso.', 'Presidía un banquete festivo.', 'Conducía un desfile por las calles de Jerusalén.'], 'answer': 'Ofrecía sacrificios para sí mismo.', 'justification': 'En este día, el sumo sacerdote ofrecía sacrificios por sus propios pecados y por los pecados de todo el pueblo.', 'type': 'multiple_choice'}, {'question': '¿Cuál es la importancia de la sangre en los sacrificios rituales mencionados en Levítico?', 'options': ['La sangre es solo un elemento simbólico sin importancia.', 'La sangre es utilizada para regar las cosechas.', 'La sangre representa la vida y se usa para la expiación.', 'La sangre es bebida como un rito ceremonial.'], 'answer': 'La sangre representa la vida y se usa para la expiación.', 'justification': 'La sangre es fundamental en la teología de sacrificios porque representa la vida y es esencial para la expiación de los pecados.', 'type': 'multiple_choice'}, {'question': '¿Qué prácticas sexuales prohibidas se mencionan en Levítico 18?', 'options': ['El matrimonio entre hermanos.', 'La poligamia.', 'La homosexualidad y el incesto.', 'El divorcio.'], 'answer': 'La homosexualidad y el incesto.', 'justification': 'Levítico 18 contiene prohibiciones sobre varias prácticas sexuales, incluyendo la homosexualidad y el incesto, entre otras.', 'type': 'multiple_choice'}, {'question': '¿Cuál es la importancia del Año de Jubileo mencionado en Levítico 25?', 'options': ['Se celebra con una gran fiesta de banquetes.', 'Es un año de guerra y conquista.', 'Significa la liberación de esclavos y la restauración de tierras.', 'Es un año de sanción y castigo divino.'], 'answer': 'Significa la liberación de esclavos y la restauración de tierras.', 'justification': 'El Año de Jubileo era un año de libertad, en el cual los esclavos eran liberados y las tierras eran devueltas a sus propietarios originales.', 'type': 'multiple_choice'}, {'question': '¿Qué significa Levítico en griego?', 'options': ['Relativo a los levitas', 'Libro de la Ley', 'Santidad', 'Libro de los Sacrificios'], 'answer': 'Relativo a los levitas', 'justification': 'El nombre Levítico se relaciona con los levitas, la tribu encargada de los rituales religiosos en Israel.', 'type': 'multiple_choice'}, {'question': '¿Quiénes son los destinatarios de Levítico?', 'options': ['El pueblo de Israel', 'Los reyes', 'Los sacerdotes', 'Los jueces'], 'answer': 'Los sacerdotes', 'justification': 'Levítico está dirigido principalmente a los sacerdotes, encargados de los rituales y de mantener la pureza en el pueblo.', 'type': 'multiple_choice'}, {'question': '¿Cuál es el propósito (A dentro del quiasmo) de Levítico?', 'options': ['Legislar el culto', 'Establecer leyes morales', 'Definir el rol del Tabernáculo', 'Detallar el éxodo de Egipto'], 'answer': 'Legislar el culto', 'justification': 'El propósito es legislar el culto y establecer las normas para la adoración y sacrificios.', 'type': 'multiple_choice'}, {'question': '¿Cuál es la estructura al principio de Levítico?', 'options': ['Ley de pureza', 'Consagración de los sacerdotes', 'Sistema sacrificial', 'Ley del diezmo'], 'answer': 'Sistema sacrificial', 'justification': 'El comienzo de Levítico trata sobre el sistema sacrificial, estableciendo las reglas para los diferentes tipos de sacrificios.', 'type': 'multiple_choice'}, {'question': '¿Cuál es la estructura en la segunda o B de Levítico?', 'options': ['Sistema sacrificial', 'Ley de pureza', 'Consagración de los sacerdotes', 'Festividades'], 'answer': 'Consagración de los sacerdotes', 'justification': 'La segunda sección se enfoca en la consagración de los sacerdotes, estableciendo su rol y responsabilidades.', 'type': 'multiple_choice'}, {'question': '¿Cuál es la estructura en la tercera o C de Levítico?', 'options': ['Sistema sacrificial', 'Pureza moral', 'Los rituales de pureza', 'Festividades'], 'answer': 'Los rituales de pureza', 'justification': 'Esta sección aborda los rituales de pureza que deben seguir los israelitas para mantener la santidad.', 'type': 'multiple_choice'}, {'question': '¿Siguiendo el quiasmo, después de C viene el:', 'options': ['A', "B'", "C'", "A'"], 'answer': 'Día de la Expiación', 'justification': 'El Día de la Expiación es el punto central del quiasmo en Levítico, enfatizando la reconciliación con Dios.', 'type': 'multiple_choice'}, {'question': "Siguiendo el quiasmo después de C' viene:", 'options': ["A'", "B'", 'Fiestas rituales', 'Requisitos para sacerdotes'], 'answer': 'Pureza moral', 'justification': "La sección de C' en el quiasmo se centra en las leyes de pureza moral, similar a los rituales de pureza.", 'type': 'multiple_choice'}, {'question': "Siguiendo el quiasmo, después de B' viene:", 'options': ['Requisitos para sacerdotes', 'Pureza ritual', 'Sistema sacrificial', 'Día de la Expiación'], 'answer': 'Requisitos para sacerdotes', 'justification': "En B', se reitera la importancia de los sacerdotes y se detallan requisitos adicionales para ellos.", 'type': 'multiple_choice'}, {'question': "Siguiendo el quiasmo, después de A' viene:", 'options': ['Pureza ritual', 'Fiestas rituales', 'Sistema sacrificial', 'Consagración'], 'answer': 'Fiestas rituales', 'justification': "La sección final A' trata de las fiestas rituales que Israel debe observar para mantener su relación con Dios.", 'type': 'multiple_choice'}, {'question': '¿Cuál fue el propósito principal de la realización de censos en el libro de Números?', 'options': ['Determinar la riqueza de las tribus.', 'Contar a los varones aptos para la milicia.', 'Establecer la herencia de las hijas de Zelofehad.', 'Registrar las enfermedades cutáneas.'], 'answer': 'Contar a los varones aptos para la milicia.', 'justification': 'El propósito de los censos en Números era preparar al pueblo para la guerra, contando a los varones mayores de 20 años aptos para la milicia.', 'type': 'multiple_choice'}, {'question': '¿Cuál fue la restricción principal impuesta a los nazareos?', 'options': ['No podían ingresar a la Tienda de reunión.', 'No podían casarse.', 'No podían consumir ningún producto de la vid.', 'No podían tocar ningún instrumento musical.'], 'answer': 'No podían consumir ningún producto de la vid.', 'justification': 'Según Números 6, los nazareos no podían consumir productos derivados de la vid como parte de su voto de consagración a Dios.', 'type': 'multiple_choice'}, {'question': '¿Qué evento puso a prueba tanto la fe del pueblo como el liderazgo de Moisés?', 'options': ['La conquista de Jericó.', 'La llegada de nuevas tribus a Israel.', 'La rebelión contra Moisés y Aarón.', 'El rechazo a la entrada en la tierra prometida.'], 'answer': 'El rechazo a la entrada en la tierra prometida.', 'justification': 'El rechazo a la entrada a la tierra prometida, debido al informe de los espías, puso a prueba la fe del pueblo y el liderazgo de Moisés (Números 13-14).', 'type': 'multiple_choice'}, {'question': '¿Por qué acción se detuvo una plaga en Israel?', 'options': ['Una plaga natural se disipó por sí sola.', 'Finees mató a un israelita y a una madianita en un acto de celo por Dios.', 'Moisés intercedió con Dios.', 'Los israelitas se arrepintieron y ofrecieron sacrificios.'], 'answer': 'Finees mató a un israelita y a una madianita en un acto de celo por Dios.', 'justification': 'En Números 25, Finees detuvo la plaga al matar a un israelita y a una madianita que habían desobedecido las leyes de Dios.', 'type': 'multiple_choice'}, {'question': '¿Qué establece Deuteronomio sobre los jueces?', 'options': ['Deben ser seleccionados entre sacerdotes.', 'Pueden dictar leyes sin consultar.', 'Son nombrados para garantizar justicia y estabilidad.', 'Solo juzgan casos de homicidio.'], 'answer': 'Son nombrados para garantizar justicia y estabilidad.', 'justification': 'Deuteronomio resalta que los jueces son responsables de impartir justicia y mantener la estabilidad social bajo la guía de las leyes divinas.', 'type': 'multiple_choice'}, {'question': '¿Qué regula Deuteronomio sobre el matrimonio y la familia?', 'options': ['La participación de sacerdotes en bodas.', 'La herencia y derechos familiares.', 'La convivencia entre tribus.', 'Los sacrificios matrimoniales.'], 'answer': 'La herencia y derechos familiares.', 'justification': 'Deuteronomio regula la herencia y derechos familiares, garantizando justicia en temas como el primogénito y el matrimonio levirato.', 'type': 'multiple_choice'}, {'question': '¿Cuál de los siguientes relatos es una mención relevante mesiánica del Deuteronomio?', 'options': ['La estrella y el cetro de Jacob.', 'La ley del perdón.', 'La promesa de un profeta como Moisés.', 'El cetro de Judá.'], 'answer': 'La promesa de un profeta como Moisés.', 'justification': 'Deuteronomio 18:15-19 menciona la promesa de un profeta como Moisés, una referencia mesiánica en el texto.', 'type': 'multiple_choice'}, {'question': '¿Qué elementos de culto incluye el código deuteronómico?', 'options': ['Ofrecimiento de sacrificios y altares dispersos.', 'Centralización de la adoración y ofrendas.', 'Adoración en varios lugares y fiestas paganas.', 'Fiestas sin reglas específicas.'], 'answer': 'Centralización de la adoración y ofrendas.', 'justification': 'Deuteronomio enfatiza la centralización del culto en un lugar específico para garantizar la pureza de la adoración.', 'type': 'multiple_choice'}, {'question': '¿Cuál es la estructura de los tratados antiguos mencionados en el texto?', 'options': ['Introducción, leyes, bendiciones y castigos.', 'Resumen, leyes y firma del rey.', 'Preámbulo, estipulaciones, bendiciones y testigos.', 'Historias antiguas, ley y profecías.'], 'answer': 'Preámbulo, estipulaciones, bendiciones y testigos.', 'justification': 'Deuteronomio sigue la estructura de los tratados antiguos, incluyendo preámbulo, estipulaciones, bendiciones y testigos.', 'type': 'multiple_choice'}, {'question': "¿Qué significa 'Levítico' en griego?", 'options': ['Relativo a los Levitas', 'Leyes del Tabernáculo', 'Sacrificios Rituales', 'Santificación'], 'answer': 'Relativo a los Levitas', 'justification': "El término 'Levítico' proviene del griego y se traduce como 'relativo a los levitas', reflejando su enfoque en las funciones y leyes asociadas a esta tribu sacerdotal.", 'type': 'multiple_choice'}, {'question': '¿Cuál es el propósito principal del libro de Números?', 'options': ['Establecer leyes para el tabernáculo', 'Relatar las peregrinaciones y pruebas de Israel en el desierto', 'Renovar el pacto con Dios', 'Establecer el quiasmo de la Ley'], 'answer': 'Relatar las peregrinaciones y pruebas de Israel en el desierto', 'justification': 'El libro de Números narra las experiencias del pueblo de Israel durante sus 40 años en el desierto, destacando la preparación para entrar en la Tierra Prometida.', 'type': 'multiple_choice'}, {'question': '¿Qué versículo define el propósito principal del libro de Levítico?', 'options': ['Levítico 19:2', 'Levítico 16:34', 'Levítico 11:45', 'Levítico 10:3'], 'answer': 'Levítico 19:2', 'justification': "Levítico 19:2 dice: 'Santos seréis, porque santo soy yo Jehová vuestro Dios', enfatizando la necesidad de una vida santa.", 'type': 'multiple_choice'}, {'question': '¿Qué estructura representa el quiasmo del libro de Levítico?', 'options': ["A-B-C-X-C'-B'-A'", "1-2-3-X-3'-2'-1'", "A-B-C-D-B'-A'", "X-A-B-C-X'"], 'answer': "A-B-C-X-C'-B'-A'", 'justification': 'El quiasmo de Levítico tiene su punto central en el Día de la Expiación (capítulo 16), con secciones paralelas antes y después.', 'type': 'multiple_choice'}, {'question': '¿Dónde se encuentra el pueblo de Israel al inicio del libro de Números?', 'options': ['Al pie del Monte Sinaí', 'En las llanuras de Moab', 'En el río Jordán', 'En Canaán'], 'answer': 'Al pie del Monte Sinaí', 'justification': 'Números comienza con el pueblo de Israel acampado en el Monte Sinaí, preparándose para el viaje hacia la Tierra Prometida.', 'type': 'multiple_choice'}, {'question': "¿Qué significado tiene el título hebreo de Deuteronomio, 'Devarim'?", 'options': ['Palabras o discursos', 'Ley renovada', 'Alianza eterna', 'Guía de los levitas'], 'answer': 'Palabras o discursos', 'justification': "El término 'Devarim' significa 'palabras o discursos', refiriéndose a los mensajes de Moisés al pueblo antes de entrar en Canaán.", 'type': 'multiple_choice'}, {'question': '¿Cuál es el marco histórico del libro de Deuteronomio?', 'options': ['El Monte Sinaí', 'El desierto de Parán', 'Las llanuras de Moab', 'El valle de Jezreel'], 'answer': 'Las llanuras de Moab', 'justification': 'Deuteronomio se desarrolla en las llanuras de Moab, donde Moisés entrega sus discursos finales antes de la entrada a Canaán.', 'type': 'multiple_choice'}, {'question': '¿Cuál es el propósito central de Deuteronomio?', 'options': ['Establecer leyes para los levitas', 'Renovar el pacto entre Dios e Israel', 'Narrar las peregrinaciones de Israel', 'Registrar el quiasmo de las leyes'], 'answer': 'Renovar el pacto entre Dios e Israel', 'justification': 'Deuteronomio busca renovar la relación entre Dios e Israel, recordando las obras divinas y exhortando a la obediencia.', 'type': 'multiple_choice'}, {'question': '¿Cuáles son las principales festividades mencionadas en el código deuteronómico?', 'options': ['Pascua, Pentecostés y Tabernáculos.', 'Día de la creación y Expiación.', 'Año nuevo y Semana Santa.', 'Fiesta de las luces y la primavera.'], 'answer': 'Pascua, Pentecostés y Tabernáculos.', 'justification': 'El código deuteronómico menciona festividades clave como Pascua, Pentecostés y Tabernáculos, que estructuran el calendario litúrgico de Israel.', 'type': 'multiple_choice'}, {'question': 'La promesa de un profeta como Moisés es una mención mesiánica relevante en el libro de Deuteronomio.', 'options': ['Verdadero', 'Falso'], 'answer': 'Verdadero', 'justification': 'Esta referencia se encuentra en Deuteronomio 18:15-19, donde se predice un profeta que será como Moisés, apuntando a una figura mesiánica clave.', 'type': 'multiple_choice'}, {'question': 'El propósito principal de las ciudades de refugio en Números 35 fue proteger a criminales fugitivos.', 'options': ['Verdadero', 'Falso'], 'answer': 'Falso', 'justification': 'Las ciudades de refugio no protegían a criminales, sino que ofrecían asilo a personas que habían cometido homicidio involuntario, asegurando un juicio justo.', 'type': 'multiple_choice'}, {'question': '¿Cuál es la restricción principal impuesta a los nazareos?', 'options': ['No podían consumir ningún producto de la vid.', 'No podían acercarse a personas enfermas.', 'No podían casarse.', 'No podían realizar sacrificios.'], 'answer': 'No podían consumir ningún producto de la vid.', 'justification': 'Según Números 6, los nazareos debían abstenerse de productos derivados de la vid como parte de su voto de consagración.', 'type': 'multiple_choice'}, {'question': 'El nombre griego del libro de Deuteronomio significa Discursos y/o Palabras.', 'options': ['Verdadero', 'Falso'], 'answer': 'Falso', 'justification': "El nombre griego 'Deuteronomio' significa 'Segunda Ley', haciendo referencia a la repetición de las leyes en el texto.", 'type': 'multiple_choice'}, {'question': '¿Qué caracteriza la guía divina del Pueblo de Israel según el texto?', 'options': ['Se basa en la astrología y la hepatoscopia.', 'Está delimitada por la Torá.', 'Se encuentra en tratados con naciones menos poderosas.', 'Es independiente de la Ley y los mandamientos.'],
"answer": "Está delimitada por la Torá.",
        "justification": "La Torá define las leyes y mandamientos que guían al pueblo en su relación con Dios y las naciones vecinas.",
        "type": "multiple_choice"
    },
    {
        "question": "El evento que marca el comienzo del libro de Números es el censo de los israelitas.",
        "options": ["Verdadero", "Falso"],
        "answer": "Verdadero",
        "justification": "El libro de Números comienza con un censo de los varones aptos para la guerra, según el mandato de Dios a Moisés.",
        "type": "multiple_choice"
    },
    {
        "question": "Explica el propósito de las ciudades de refugio en Números 35.",
        "type": "open",
        "justification": "Estas ciudades servían para dar asilo a quienes mataban accidentalmente a alguien, evitando venganzas injustas y permitiendo un juicio justo."
    }
]                                                                                                                                                                                                                                                                                                                                                                                                                                                  
# Inicializar variables
score = 0
incorrect_questions = []

# Título del cuestionario
st.title("Cuestionario de Repaso Bíblico")

# Mostrar cada pregunta
for idx, question in enumerate(questions):
    st.write(f"### Pregunta {idx + 1}")
    st.write(question["question"])

    if question["type"] == "multiple_choice":
        # Preguntas de opción múltiple
        user_answer = st.radio(
            label="Selecciona una respuesta:",
            options=question["options"],
            key=f"question_{idx}"
        )
        if st.button(f"Validar respuesta {idx + 1}", key=f"validate_{idx}"):
            if user_answer == question["answer"]:
                st.success("¡Correcto!")
                st.write(f"Justificación: {question['justification']}")
                score += 1
            else:
                st.error(f"Incorrecto. La respuesta correcta es: {question['answer']}")
                st.write(f"Justificación: {question['justification']}")
                incorrect_questions.append(question)

    elif question["type"] == "open":
        # Pregunta abierta
        user_answer = st.text_area("Escribe tu respuesta aquí:", key=f"question_{idx}")
        if st.button(f"Mostrar respuesta {idx + 1}", key=f"validate_{idx}"):
            st.write(f"Tu respuesta: {user_answer}")
            st.info(f"Respuesta esperada: {question['justification']}")
            # Las preguntas abiertas no afectan el puntaje

    elif question["type"] == "matching":
        # Pregunta de emparejamiento
        st.write("Opciones:")
        for option in question["options"]:
            st.write(option)
        st.write("Significados:")
        for pair in question["pairs"]:
            st.write(pair)

        user_answers = {}
        for key in question["answer"]:
            user_input = st.selectbox(
                f"Emparejamiento para {key}:",
                [pair[0] for pair in [p.split(". ", 1) for p in question["pairs"]]],
                key=f"question_{idx}_{key}"
            )
            user_answers[key] = user_input

        if st.button(f"Validar emparejamiento {idx + 1}", key=f"validate_{idx}"):
            if user_answers == question["answer"]:
                st.success("¡Correcto!")
                st.write(f"Justificación: {question['justification']}")
                score += 1
            else:
                st.error("Incorrecto. Las respuestas correctas eran:")
                for k, v in question["answer"].items():
                    st.write(f"{k} -> {v}")
                st.write(f"Justificación: {question['justification']}")
                incorrect_questions.append(question)

    else:
        st.error("Tipo de pregunta no reconocido.")

# Mostrar el puntaje final
st.write(f"## Tu puntaje total es: {score}/{len(questions)}")

# Opción para reintentar preguntas incorrectas
if incorrect_questions:
    if st.button("Reintentar preguntas incorrectas"):
        for idx, question in enumerate(incorrect_questions):
            st.write(f"### Reintento - Pregunta {idx + 1}")
            st.write(question["question"])

            if question["type"] == "multiple_choice":
                user_answer = st.radio(
                    label="Selecciona una respuesta:",
                    options=question["options"],
                    key=f"retry_question_{idx}"
                )
                if st.button(f"Validar respuesta {idx + 1}", key=f"retry_validate_{idx}"):
                    if user_answer == question["answer"]:
                        st.success("¡Correcto!")
                        st.write(f"Justificación: {question['justification']}")
                        score += 1
                    else:
                        st.error(f"Incorrecto. La respuesta correcta es: {question['answer']}")
                        st.write(f"Justificación: {question['justification']}")

            elif question["type"] == "matching":
                st.write("Opciones:")
                for option in question["options"]:
                    st.write(option)
                st.write("Significados:")
                for pair in question["pairs"]:
                    st.write(pair)

                user_answers = {}
                for key in question["answer"]:
                    user_input = st.selectbox(
                        f"Emparejamiento para {key}:",
                        [pair[0] for pair in [p.split(". ", 1) for p in question["pairs"]]],
                        key=f"retry_question_{idx}_{key}"
                    )
                    user_answers[key] = user_input

                if st.button(f"Validar emparejamiento {idx + 1}", key=f"retry_validate_{idx}"):
                    if user_answers == question["answer"]:
                        st.success("¡Correcto!")
                        st.write(f"Justificación: {question['justification']}")
                        score += 1
                    else:
                        st.error("Incorrecto. Las respuestas correctas eran:")
                        for k, v in question["answer"].items():
                            st.write(f"{k} -> {v}")
                        st.write(f"Justificación: {question['justification']}")
            else:
                st.error("Tipo de pregunta no reconocido.")
else:
    st.write("¡Felicitaciones! No tienes preguntas incorrectas para reintentar.")
