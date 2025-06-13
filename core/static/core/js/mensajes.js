function eliminarProductoCarrito(id) {
    Swal.fire({
        title: '¿Desea eliminar este Producto del carrito?',
        icon: 'warning', 
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Confirmar',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire('Eliminado!', 'Producto Eliminado Correctamente', 'success').then(function() {
                window.location.href = "/eliminar_del_carrito/" + id + "/";
            });
        }
    });
}

function ModificarPerfilUsuario() {
    Swal.fire({
        title: '¿Desea modificar su usuario?',
        icon: 'warning', 
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Confirmar',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire('Modificado!', '¡Su perfil ha sido modificado con éxito!', 'success').then(function() {
                window.location.href = "/perfil_usuario/";
            });
        }
    });
}

function ModificarUsuarioAdmin() {
    Swal.fire({
        title: '¿Desea modificar el usuario?',
        icon: 'warning', 
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Confirmar',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire('Modificado!', '¡El usuario ha sido modificado con éxito!', 'success').then(function() {
                window.location.href = "/modificar_usuario/";
            });
        }
    });
}

function AgregarUsuarioAdmin() {
    Swal.fire({
        title: '¿Desea agregar un usuarion nuevo usuario?',
        icon: 'warning', 
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Confirmar',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire('Agregado!', '¡El usuario ha sido agregado con éxito!', 'success').then(function() {
                window.location.href ="/gestion_usuarios/";
            });
        }
    });
}


function eliminarUsuarioAdmin(id) {
    Swal.fire({
        title: '¿Desea eliminar este Usuario?',
        icon: 'warning', 
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Confirmar',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire('Eliminado!', 'Usuario Eliminado Correctamente', 'success').then(function() {
                window.location.href = "/eliminar_usuario/" + id + "/";
            });
        }
    });
}