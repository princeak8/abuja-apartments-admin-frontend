<template>
    <div>
        <Navbar />
        <div class="flex">
            <div class="flex-1">
                <SideBar />
            </div>
            <div class="">
                <slot></slot>
            </div>
        </div>
        
        <h3>Footer</h3>
    </div>
</template>